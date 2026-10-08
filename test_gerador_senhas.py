import string
import unittest

from gerador_senhas import CARACTERES_AMBIGUOS, gerar_senha


class GerarSenhaTests(unittest.TestCase):
    def test_gera_senha_com_tamanho_e_todas_as_classes(self):
        senha = gerar_senha(comprimento=24)

        self.assertEqual(len(senha), 24)
        self.assertTrue(any(caractere in string.ascii_lowercase for caractere in senha))
        self.assertTrue(any(caractere in string.ascii_uppercase for caractere in senha))
        self.assertTrue(any(caractere in string.digits for caractere in senha))
        self.assertTrue(any(caractere in string.punctuation for caractere in senha))

    def test_respeita_classes_desabilitadas(self):
        senha = gerar_senha(
            comprimento=16,
            incluir_minusculas=False,
            incluir_maiusculas=False,
            incluir_simbolos=False,
        )

        self.assertTrue(all(caractere in string.digits for caractere in senha))

    def test_remove_caracteres_ambiguos(self):
        senha = gerar_senha(comprimento=100, excluir_ambiguos=True)

        self.assertTrue(set(senha).isdisjoint(CARACTERES_AMBIGUOS))

    def test_rejeita_comprimento_menor_que_classes_selecionadas(self):
        with self.assertRaises(ValueError):
            gerar_senha(comprimento=3)

    def test_rejeita_quando_nenhuma_classe_e_selecionada(self):
        with self.assertRaises(ValueError):
            gerar_senha(
                incluir_minusculas=False,
                incluir_maiusculas=False,
                incluir_numeros=False,
                incluir_simbolos=False,
            )


if __name__ == "__main__":
    unittest.main()
