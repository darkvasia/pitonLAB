import random
import unittest

def charivna_kulka(question):
    """
    Функція для імітації "чарівної кульки передбачень".
    
    Параметри:
    question (str): Питання, на яке потрібно отримати відповідь.
    
    Повертає:
    str: Одну з можливих відповідей або повідомлення про помилку, якщо введення некоректне.
    
    Приклад використання:
    >>> charivna_kulka("Чи буду я щасливий?")
    'Можливо'
    """
    if not isinstance(question, str) or not question.strip():
        return "Будь ласка, задайте питання."
    responses = ["Так", "Ні", "Можливо", "Скоріше за все", "Важко сказати", "Попробуй знову"]
    return random.choice(responses)

class TestCharivnaKulka(unittest.TestCase):
    
    def test_response_is_in_list(self):
        question = "Чи буде завтра дощ?"
        response = charivna_kulka(question)
        self.assertIn(response, ["Так", "Ні", "Можливо", "Скоріше за все", "Важко сказати", "Попробуй знову"])

    def test_response_is_str(self):
        question = "Чи отримаю я підвищення?"
        self.assertIsInstance(charivna_kulka(question), str)

    def test_empty_question(self):
        self.assertEqual(charivna_kulka(""), "Будь ласка, задайте питання.")

    def test_non_string_input(self):
        self.assertEqual(charivna_kulka(123), "Будь ласка, задайте питання.")
        self.assertEqual(charivna_kulka(None), "Будь ласка, задайте питання.")
        self.assertEqual(charivna_kulka([]), "Будь ласка, задайте питання.")


if __name__ == '__main__':
    unittest.main()