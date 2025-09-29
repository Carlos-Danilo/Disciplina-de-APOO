from dao.ItemDAO import ItemDAO
from model.Item import Item
from typing import List

class ItemController:
    def __init__(self, dao: ItemDAO):
        self.dao = dao

    def criarItem(self, descricao: str, quantidade: int):
        item = Item(id=None, descricao=descricao, quantidade=quantidade)
        self.dao.adicionar(item)

    def obterTodosOsItens(self) -> List[Item]:
        return self.dao.listarTodos()
