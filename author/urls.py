from django.urls import path
from author.views import (
    list_author,
    create_author,
    read_author,
    update_author,
    delete_author

)

urlpatterns=[
    path("list/", list_author, name="list_author"),
    path("create/", create_author, name="create_author"),
    path("read/<id>", read_author, name="read_author"),
    path("update/<id>", update_author, name="update_author"),
    path("delete/<id>", delete_author, name="delete_author"),
]