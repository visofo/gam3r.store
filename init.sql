-- Permitir que o PostgreSQL escute em todas as interfaces de rede
ALTER SYSTEM SET listen_addresses = '*';

-- Reinicie as configurações para aplicar as mudanças
SELECT pg_reload_conf();


-- Criar o schema "public"
CREATE SCHEMA IF NOT EXISTS public;

-- Definir o schema público como padrão
SET search_path TO public;

-- Conceder permissões ao usuário do PostgreSQL
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO usuario;
