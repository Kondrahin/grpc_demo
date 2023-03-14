from loguru import logger

import grpc_demo_pb2_grpc
import grpc_demo_pb2
import grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = grpc_demo_pb2_grpc.RouteDemoStub(channel)
        print("1. Create Item")
        print("2. Get Item by ID")
        print("3. Get Items list by page")
        print("4. Update Item by ID")
        print("5. Delete Item by ID")
        while True:
            rpc_call = input("Which rpc would you like to make: ")

            if rpc_call == "1":
                item_title = input("Enter item's title: ")
                item_to_create = grpc_demo_pb2.CreateItemSchema(title=item_title)
                item = stub.CreateItem(item_to_create)
                logger.success("Item was successfully created!")
                logger.success(item)

            elif rpc_call == "2":
                item_id = input("Enter item's id: ")
                item_id_to_get = grpc_demo_pb2.ItemId(id=item_id)
                try:
                    item = stub.GetItem(item_id_to_get)
                    logger.success("Item was successfully pulled!")
                    logger.success(item)
                except grpc.RpcError as e:
                    logger.error(e.details())

            elif rpc_call == "3":
                try:
                    page = int(input("Enter page: "))
                    page_length = int(input("Enter page length: "))
                except ValueError:
                    logger.error("Enter the number!")
                    continue

                if any([page, page_length]) < 1:
                    logger.error("Numbers must be positive")
                    continue

                list_item_pagination = grpc_demo_pb2.ListItemsPagination(page=page, page_length=page_length)
                list_items = stub.ListItems(list_item_pagination)
                logger.success("Items was successfully pulled!")
                logger.success(list_items)

            elif rpc_call == "4":
                item_id = input("Enter item's id which title you want to change: ")
                item_title = input("Enter new item's title: ")
                item_update = grpc_demo_pb2.UpdateItemSchema(id=item_id, title=item_title)
                try:
                    item = stub.UpdateItem(item_update)
                    logger.success("Item was successfully updated!")
                    logger.success(item)
                except grpc.RpcError as e:
                    logger.error(e.details())

            elif rpc_call == "5":
                item_id = input("Enter item's id which you want to delete: ")
                item_id_to_delete = grpc_demo_pb2.ItemId(id=item_id)
                logger.success(item_id_to_delete)
                stub.DeleteItem(item_id_to_delete)
                logger.success(f"Item {item_id} successfully deleted")


if __name__ == "__main__":
    run()
