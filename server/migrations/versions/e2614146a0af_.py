"""empty message

Revision ID: e2614146a0af
Revises: 5bd2e2c3d74f
Create Date: 2020-06-02 19:17:23.618461

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2614146a0af'
down_revision = '5bd2e2c3d74f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('executables',
    sa.Column('uuid', sa.Text(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('command', sa.Text(), nullable=True),
    sa.Column('arguments', sa.Text(), nullable=True),
    sa.Column('env_vars', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('is_archived', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('executables')
    # ### end Alembic commands ###
