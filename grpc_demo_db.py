import json
import uuid
from datetime import datetime
from typing import Any

import grpc
import redis

import grpc_demo_pb2_grpc
import grpc_demo_pb2


def item_not_found_error(item_id: str, context: Any):
    msg = f"Item with id '{item_id}' doesn't exist"
    context.set_details(msg)
    context.set_code(grpc.StatusCode.NOT_FOUND)
    return grpc_demo_pb2.Item()


def sort_items_by_created_at(items_list: list[grpc_demo_pb2.Item]):
    return sorted(items_list, key=lambda x: datetime.fromisoformat(x.created_at))


class DemoRepo:
    def __init__(self):
        pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
        self.redis = redis.Redis(connection_pool=pool)

    def create_item(self, item: grpc_demo_pb2.CreateItemSchema):
        item_id = str(uuid.uuid4())
        created_at = str(datetime.now())
        self.redis.set(item_id, json.dumps(
            {"title": item.title, "created_at": created_at}, default=str)
                       )
        return grpc_demo_pb2.Item(
            id=item_id, title=item.title, created_at=created_at
        )

    def get_item(self, item_id: grpc_demo_pb2.ItemId, context: Any):
        item = self.redis.get(item_id.id)
        if not item:
            return item_not_found_error(item_id.id, context)
        item = json.loads(item)
        return grpc_demo_pb2.Item(
            id=item_id.id, title=item["title"], created_at=item["created_at"]
        )

    def get_items(self, list_item_pagination: grpc_demo_pb2.ListItemsPagination):
        items_keys = self.redis.keys()
        items = []
        for key in items_keys:
            item = json.loads(self.redis.get(key))
            item_schema = grpc_demo_pb2.Item(
                id=key, title=item["title"], created_at=item["created_at"]
            )
            items.append(item_schema)
        items = sort_items_by_created_at(items)
        result = items[
                 (list_item_pagination.page-1)*list_item_pagination.page_length
                 :list_item_pagination.page*list_item_pagination.page_length:
            ]
        return grpc_demo_pb2.ListItemsSchema(items=result)

    def update_item(self, item_to_update: grpc_demo_pb2.UpdateItemSchema, context: Any):
        item = self.redis.get(item_to_update.id)
        if not item:
            return item_not_found_error(item_to_update.id, context)
        item = json.loads(item)
        self.redis.set(
            item_to_update.id,
            json.dumps({"title": item_to_update.title, "created_at": item["created_at"]}, default=str)
        )
        return grpc_demo_pb2.Item(
            id=item_to_update.id, title=item_to_update.title, created_at=item["created_at"]
        )

    def delete_item(self, item_id: grpc_demo_pb2.ItemId):
        self.redis.delete(str(item_id.id))
