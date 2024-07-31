"""alterando o Product_code

Revision ID: 0580d722b200
Revises: e437219f8815
Create Date: 2024-07-30 21:21:55.375407

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0580d722b200'
down_revision = 'e437219f8815'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        # Renomear a coluna 'Product_code' para 'product_code'
        batch_op.alter_column(
            'Product_code',
            new_column_name='product_code',
            existing_type=sa.String(length=90),
            existing_nullable=False
        )
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        # Reverter a mudança, renomeando 'product_code' de volta para 'Product_code'
        batch_op.alter_column(
            'product_code',
            new_column_name='Product_code',
            existing_type=sa.String(length=90),
            existing_nullable=False
        )