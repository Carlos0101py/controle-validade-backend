"""mudança na tabela produto

Revision ID: cba8a5cc7239
Revises: 1bacf4a28572
Create Date: 2024-08-06 23:03:26.838520

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cba8a5cc7239'
down_revision = '1bacf4a28572'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_constraint('product_ibfk_2', type_='foreignkey')
        batch_op.drop_column('situation')

    op.drop_table('situation_product')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('situation', mysql.VARCHAR(length=100), nullable=False))
        batch_op.create_foreign_key('product_ibfk_2', 'situation_product', ['situation'], ['id'])

    op.create_table('situation_product',
    sa.Column('name', mysql.VARCHAR(length=45), nullable=False),
    sa.Column('id', mysql.VARCHAR(length=36), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
