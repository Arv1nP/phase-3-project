"""Progress and user table seprate

Revision ID: d9d673e3595f
Revises: cb192ff2e151
Create Date: 2024-05-19 21:39:22.399207

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd9d673e3595f'
down_revision: Union[str, None] = 'cb192ff2e151'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('progress',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('words_learned_en', sa.Integer(), nullable=True),
    sa.Column('words_learned_fr', sa.Integer(), nullable=True),
    sa.Column('words_learned_it', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['username'], ['users.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('users', 'words_learned_en')
    op.drop_column('users', 'words_learned_it')
    op.drop_column('users', 'words_learned_fr')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('words_learned_fr', sa.INTEGER(), nullable=True))
    op.add_column('users', sa.Column('words_learned_it', sa.INTEGER(), nullable=True))
    op.add_column('users', sa.Column('words_learned_en', sa.INTEGER(), nullable=True))
    op.drop_table('progress')
    # ### end Alembic commands ###