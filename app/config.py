from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_hostname: str 
    database_port: str 
    database_password : str 
    database_name: str
    database_username: str
    secret_key: str
    algorithm : str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"

    @property
    def database_url(self):
        return f"postgresql://{self.database_username}:{self.database_password}@{self.database_hostname}:{self.database_port}/{self.database_name}"


settings = Settings()    

