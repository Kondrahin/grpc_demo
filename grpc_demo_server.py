from concurrent import futures
import logging
from typing import Any


import grpc
import grpc_demo_pb2_grpc
import grpc_demo_pb2
from grpc_demo_db import DemoRepo


class RoutDemoServicer(grpc_demo_pb2_grpc.RouteDemoServicer):
    """Provides methods that implement functionality of route demo server."""

    def __init__(self):
        self.repo = DemoRepo()

    def CreateItem(self, request: grpc_demo_pb2.CreateItemSchema, context: Any):
        item = self.repo.create_item(request)
        return item

    def GetItem(self, request: grpc_demo_pb2.ItemId, context: Any):
        item = self.repo.get_item(request, context)
        return item

    def ListItems(self, request: grpc_demo_pb2.ListItemsPagination, context: Any):
        list_items = self.repo.get_items(request)
        return list_items

    def UpdateItem(self, request: grpc_demo_pb2.UpdateItemSchema, context):
        return self.repo.update_item(request, context)

    def DeleteItem(self, request: grpc_demo_pb2.ItemId, context: Any):
        self.repo.delete_item(request)
        return grpc_demo_pb2.Empty()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_demo_pb2_grpc.add_RouteDemoServicer_to_server(
        RoutDemoServicer(), server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
