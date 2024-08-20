"""atualizadno campo do group

Revision ID: a657d8f1727f
Revises: e059c66524d7
Create Date: 2024-08-19 22:35:46.063166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a657d8f1727f'
down_revision = 'e059c66524d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('group', schema=None) as batch_op:
        batch_op.add_column(sa.Column('creator_id', sa.String(length=100), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('group', schema=None) as batch_op:
        batch_op.drop_column('creator_id')

    # ### end Alembic commands ###
