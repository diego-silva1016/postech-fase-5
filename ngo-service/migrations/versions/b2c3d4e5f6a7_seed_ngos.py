"""seed ngos

Revision ID: b2c3d4e5f6a7
Revises: a1b2c3d4e5f6
Create Date: 2026-07-02 21:00:01.000000

"""
from alembic import op


revision = "b2c3d4e5f6a7"
down_revision = "a1b2c3d4e5f6"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        INSERT INTO ngos (name, email, cause, city) VALUES
            ('Anjos de Patas', 'contato@anjosdepatas.org', 'Proteção Animal', 'Osasco'),
            ('Educa Mais', 'info@educamais.org', 'Educação', 'São Paulo')
        ON CONFLICT (email) DO NOTHING
        """
    )


def downgrade():
    op.execute(
        """
        DELETE FROM ngos
        WHERE email IN ('contato@anjosdepatas.org', 'info@educamais.org')
        """
    )
