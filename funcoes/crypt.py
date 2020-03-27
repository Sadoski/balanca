# -*- coding: utf-8 -*-
"""
Modulo especifico de criptografia e descryptografia
"""
import os, base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import load_pem_private_key


class Crypt:
    """
    Classe de Criptografia e Descryptografia de dados e arquivos
    """
    def generate_private_key(self):
        """
        Metodo para gerar chave privada
        Retorno:
            - Retorna a chave privada
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=4096,
            backend=default_backend()
        )
        return private_key

    def generate_public_key(self, private_key):
        """
        Metodo para gerar chave publica
        Parâmetro:
            - private_key: chave privada
        Retorno;
            - Retorna a chave publica
        Exceção:
            - Caso a chave privada não possa ser convertida em privada mostre a mensagem de erro e retorne falso
        """
        try:
            public_key = private_key.public_key()
            return public_key
        except:
            print("Erro ao criar chave publica")
            return False

    def generate_salt(self):
        """
        Metodo para gerar um salto
        Retorno:
            - Retorna o salto
        """
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend())
        key_fernet = Fernet.generate_key()
        key = base64.urlsafe_b64encode(kdf.derive(key_fernet))
        return key.decode('utf-8')

    def save_key(self, private_key, file_name):
        """
        Medoto para savar a chave privada em arquivo
        Parãmetro:
            - private_key: chave privada
            - file_name: nome, extenção e diretorio do arquivo
        Exceção:
            - Caso não consida converter a chave privada ou salvar-la no arquivo, apresente a mensagem de erro
        """
        try:
            pem = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )
            with open(file_name, 'wb') as file_out:
                file_out.write(pem)
            file_out.close()
        except:
            print("Erro ao salvar a chave privada no arquivo")

    def save_file(self, cipher_text: bytes, file_name):
        """
        Metodo para savar o dados criptografados em arquivo
        Parâmetro:
            - cipher_text: dados criptorgrafados
            - file_name: nome, extenção e diretorio do arquivo
        Exceção:
            - Caso não consiga salvar o arquivo exiba a mendagem de erro
        """
        try:
            with open(file_name, 'wb') as file_out:
                file_out.write(cipher_text)
            file_out.close()
        except:
            print("Erro ao salvar os dados no arquivo")

    def open_key(self, file_name):
        """
        Metodo para ler informações do arquivo da chave privada
        Parâmetro:
            - file_name: nome, extenção e diretorio do arquivo
        Retorno:
            - Retorna os dados da chave privada do arquivo
        Exceção:
            - Caso não consiga ler o arquivo e transformar em classe ... apresente o erro e retorne falso
        """
        try:
            with open(file_name, 'rb') as file_input:
                file_pem = file_input.read()
            private_key = load_pem_private_key(file_pem, None, default_backend())
            return private_key
        except:
            print("Erro ao ler dados dos arquivos da chave privada")
            return False

    def open_file(self, file_name):
        """
        Metodo para ler os dados dos arquivos
        Parâmetro:
            - file_name: nome, extenção e diretorio do arquivo
        Retorno:
            - Retorna os dados do arquivo
        """
        try:
            with open(file_name, 'r') as file_input:
                file_pem = file_input.read()
            return file_pem
        except:
            print("Erro ao ler dados dos arquivos")
            return False

    def encryptions_asymmetric(self, text: str, public_key):
        """
        Metodo para criptografar os dado
        Parâmetro:
            - text: dados em texto a ser criptografados
            - public_key: chave publica
        Retorno:
            - Retorna os dados criptografados
        Exceção:
            - Caso não consiga criptografar os dado, apresente a mesagem de erro e retorne falso
        """
        try:
            cipher_text_bytes = public_key.encrypt(
                plaintext=text.encode('utf-8'),
                padding=padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA512(),
                    label=None
                )
            )
            cipher_text = base64.urlsafe_b64encode(cipher_text_bytes)
            return cipher_text
        except:
            print("Erro ao criptogravar dados")
            return False

    def decryptions_asymmetric(self, cipher_text: str, private_key):
        """
        Metodo para descriptografar os dado
        Parâmetro:
            - cipher_text: dados criptografados
            - private_key: chave privada
        Retorno:
            - Retorna os dados descriptografados
        Exceção:
            - Caso não consiga descriptografar os dado, apresente a mesagem de erro e retorne falso
        """
        try:
            decrypted_cipher_text_bytes = private_key.decrypt(
                ciphertext=base64.urlsafe_b64decode(cipher_text),
                padding=padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA512(),
                    label=None
                )
            )
            decrypted_cipher_text = decrypted_cipher_text_bytes.decode('utf-8')
            return decrypted_cipher_text
        except:
            print("Erro ao descriptografar")
            return False

    def encrypt(self, text: str, salt: str) -> str:
        """
        Metodo para criptografar o texto informado
        Parametros:
            - text: dados de texto
            - salt: dados do salto
        Retorno:
            - Retorna o texto criptografado
        Exceção:
            - Caso não consiga criptografar os dado, apresente a mesagem de erro e retorne falso
        """
        try:
            fernet = Fernet(salt.encode('utf8'))
            encrypted = fernet.encrypt(text.encode('utf8'))
            return base64.urlsafe_b64encode(encrypted).decode('utf-8')
        except:
            print("Erro ao criptografar o dado")
            return False

    def decrypt(self, text: str, salt: str) -> str:
        """
        Metodo para descriptografar o texto informado
        Parametros:
            - text: dados de texto
            - salt: dados do salto
        Retorno:
            - Retorna o texto descriptografado
        Exceção:
            - Caso não consiga descriptografar os dado, apresente a mesagem de erro e retorne falso
        """
        try:
            fernet = Fernet(salt.encode('utf8'))
            decrypted = base64.urlsafe_b64decode(text.encode('utf8'))

            return fernet.decrypt(decrypted).decode('utf-8')
        except:
            print("Erro ao descriptografar o dado")
            return False

    def encrypt_file(self, file_name, salt: str):
        """
        Metodo para criptografar o texto informado
        Parametros:
            - text: dados de texto
            - salt: dados do salto
        Retorno:
            - Retorna o texto criptografado
        Exceção:
            - Caso não consiga criptografar os dados do arquivo, apresente a mesagem de erro
        """
        try:
            fernet = Fernet(salt.encode('utf8'))
            file_encrypted = fernet.encrypt(file_name)

            return file_encrypted
        except:
            print("Erro ao criptografar o arquivo")
            return False

    def descrypt_file(self, file_name, salt: str):
        """
        Metodo para criptografar o texto informado
        Parametros:
            - text: dados de texto
            - salt: dados do salto
        Retorno:
            - Retorna o texto descriptografado
        Exceção:
            - Caso não consiga descriptografar os dado, apresente a mesagem de erro e retorne falso
        """
        try:
            fernet = Fernet(salt.encode('utf8'))
            file_decrypted = fernet.decrypt(file_name)

            return file_decrypted.decode('utf-8')
        except:
            print("Erro ao descriptografar o arquivo")
            return False

    def encrypt_base_64(self, senha: str) -> str:
        """
        Metodo para criptografar o texto informado
        Parametros:
            - senha: dados da senha
        Retorno:
            - Retorna o senha criptografado
        Exceção:
            - Caso não consiga criptografar os dado, apresente a mesagem de erro e retorne falso
        """
        try:
            return base64.urlsafe_b64encode(senha.encode('utf-8')).decode('utf-8')
        except:
            print("Erro ao criptografar o dado")
            return False

    def decrypt_base_64(self, senha: str) -> str:
        """
        Metodo para descriptografar o texto informado
        Parametros:
            - senha: dados do salto
        Retorno:
            - Retorna o senha descriptografado
        Exceção:
            - Caso não consiga descriptografar os dado, apresente a mesagem de erro e retorne falso
        """
        try:
            return base64.urlsafe_b64decode(senha.encode('utf8')).decode('utf-8')
        except:
            print("Erro ao descriptografar o dado")
            return False