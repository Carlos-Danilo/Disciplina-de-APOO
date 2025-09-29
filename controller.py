from dao import ItemDAO
from model import Item
from typing import List

class ItemController:
    def __init__(self, dao : ItemDAO):
        self.dao = dao

    def criarItem(self, descricao: str, quantidade: int):
        novo_item = Item(id=None, descricao=descricao, quantidade=quantidade)
        self.dao.adicionar(novo_item)

    def obterTodosOsItens(self) -> List[Item]:
        return self.dao.listarTodos()