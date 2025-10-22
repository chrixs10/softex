import hashlib


def hash_senha(senha: str) -> str:
    """Gera um hash SHA-256 da senha."""
    return hashlib.sha256(senha.encode("utf-8")).hexdigest()


def verificar_senha(senha_digitada: str, hash_armazenado: str) -> bool:
    """Verifica se a senha digitada corresponde ao hash no banco."""
    return hash_senha(senha_digitada) == hash_armazenado

senha = "botafogo"
senha_hash = hash_senha(senha)
print(senha_hash)

senha_alternativa = "ded6a687514227ff822d40bd397f30f5ae9132487ad6c846599131c740d784f0"
print(verificar_senha(senha, senha_alternativa))