
# user_service.py
from user_model import UserModel
from hasher import hash_senha, verificar_senha


class UserService:

    def __init__(self):
        """
        crie um atributo que receberá a UserModel como composição
        """

    def _safe_user_data(self, user) -> dict | None:
        """
        este é um método privado que recebe um usuarios do banco.
        verifique se o usuários existe e então retorne ele sem a sua senha
        caso ele ão exista retorne None
        """
        if user:
            return{
                'id': user['id'],
                'email':user['email'],
                'nome_completo':user['nome_completo'],
                'perfil_acesso':user['perfil_acesso'],
                'data_criacao':user['data_criacao'],
                'data_atualizacao':user['data_atualizacao']
            }
        else:
            return None
        

    def _is_authorized(
        self,
        current_user_id: int | None,
        current_user_profile: str,
        target_user_id: int,
        action: str,
    ) -> bool:
        """
        Método que verifica o perfil do usuários, se for Diretoria retorne true
        Se não tiver target_user_id retorn false
        Se  action == "edit_self" retorne current_user_id == target_user_id
        No geral retorn false
        """
        if current_user_id == "Diretoria":
            return True
        if not target_user_id:
            return False
        if action == "edit_self":
            return current_user_id == target_user_id
        else:
            return False
        
    def register_user(
        self,
        senha: str,
        email: str,
        nome_completo: str,
        perfil: str = "Afiliado",
    ) -> tuple[bool, str]:
        """
        Método para criar um usuários.
        o campo senha deve ter no mínimo 8 caracteres, caso contrário retorne False a mensagem de erro.
        O campo email deve ter pelo menos 10 caracteres, uma @ e terminar com .com, retorne False se não tiver e a mensagem de erro.
        O campo Nome deve ter apenas letras e não deve estar vazio, retorne False se não tiver e a mensagem de erro.
        Caso os campos atendas as requisições, faça o hash da senha e salve use o método create_user da User Model
        """
        if not nome_completo or not nome_completo.replace(" ", "").isalpha():
            return False, "O nome deve conter apenas letras e e nao pode estar vazio."
        if not email  or len(email) < 10 or "@" not in email:
            return False, "Email inválido. deve ter ao menos 10 caracteres, conter '@' e terminar com '.com'."
        if not senha or len(senha) < 8:
            return False, "A senha deve conter apenas 8 caracteres"

    def login_user(self, email: str, senha: str) -> tuple[dict | None, str]:
        """
        Este método é o login do usuários, deve receber um email e senha não vazios
        Use o método do find_user_by_email para buscar o usuario
        Se houver usuarios faça a comparação da senha passada com a senha hash do DB
        Use a função verificar_senha, se tiver ok, retorne o usuarios pelo método privado _safe_user_data
        e a mensagem Login bem-sucedido!.
        Caso contrario retorne None e a mensagem de erro
        """
        if not email or not senha:
            return None, "E-mail e senha são obrigatórios"

        user = self.user_model.find_user_by_email(email)
        if not user:
            return None, "E-mail e senha incorretos!"

        if verificar_senha(senha, user['senha']):
            return self._safe_user_data(user), "login bem-sucedido!"
        else:
            return None, "E-mail ou senha incorretos." 

    def update_user_profile(
        self,
        current_user_id: int | None,
        current_user_profile: str,
        target_user_id: int,
        new_data: dict,
    ) -> tuple[bool, str]:
        """
        Método para atualizar usuários.
        Chame o método privado _is_authorized, se o retorno for false, retorne false e acesso negado
        Confira as chaves em new_data (senha, nome_completo, email), se pelo menos um desses campos,
        Caso não haja nenhum valor a ser atualizado, encerre a função com False e mensagem de erro.
        Caso contrátio, chame o método da UserModel update_user_by_id passando o id e o new data
        """
        if not self._is_authorized(current_user_id, current_user_profile, target_user_id):
            return False, "Acesso Negado"
        

    def delete_user(
        self,
        current_user_profile: str,
        user_id: int,
    ) -> tuple[bool, str]:
        """
        Método para deletar usuarios.
        So é permitido deletar usuarios se o current_user_profile for Diretoria.
        Caso não seja retorn false e a mensagem de acesso negado
        Senão chame o método delete_user_by_id, passando o id do usuários
        """
        if current_user_profile == "Diretoria":
            return True
        else:
            return False, "Acesso Negado"
        

    def get_user_by_id(self, user_id: int) -> dict | None:
        """
        Método para pegar um usuarios pelo id
        Retorne o usuarios apos passar pelo método _safe_user_data
        """

    def get_all_users(self) -> list[dict | None]:
        """
        Método para retornar todos os usuários.
        retorne todos os usuáriso apos passar pelo método _safe_user_data
        """
