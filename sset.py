#!/usr/bin/env python3

"""
Suffix tree to search in dictionary
"""

from typing import List


class SuffixTreeNode:
    def __init__(self):
        self.children = {}  # Словарь для хранения дочерних узлов
        self.indexes = []  # Список для хранения индексов слов, содержащих текущий суффикс


class SuffixTree:
    def __init__(self):
        self.root = SuffixTreeNode()  # Корень суффиксного дерева

    def insert(self, word, index):
        # Вставка всех суффиксов слова в суффиксное дерево
        for i in range(len(word)):
            current = self.root
            # Вставка суффикса, начиная с текущей позиции i
            for char in word[i:]:
                if char not in current.children:
                    current.children[char] = SuffixTreeNode()
                current = current.children[char]
                current.indexes.append(index)  # Добавление индекса слова к текущему узлу

    def search(self, substring):
        # Поиск подстроки в суффиксном дереве
        current = self.root
        for char in substring:
            if char not in current.children:
                return []  # Подстрока не найдена
            current = current.children[char]
        return current.indexes  # Возврат индексов слов, содержащих подстроку


class SSet:
    def __init__(self, fname: str) -> None:
        self.fname = fname
        self.words = []  # Список для хранения слов из файла
        self.suffix_tree = SuffixTree()  # Суффиксное дерево для поиска подстрок

    def load(self) -> None:
        # Загрузка слов из файла
        with open(self.fname, 'r') as f:
            self.words = [line.rstrip() for line in f]  # Чтение и удаление завершающих пробелов
        for index, word in enumerate(self.words):
            self.suffix_tree.insert(word, index)  # Вставка слова в суффиксное дерево

    def search(self, substring: str) -> List[str]:
        # Поиск подстроки в словах
        indexes = self.suffix_tree.search(substring)
        return [self.words[i] for i in indexes]  # Возврат слов, содержащих подстроку
