"""New Table bank,address,faqs,contact,debt,home_carousel,company_setting,delivery_p_s,special_offer,wish_list

Revision ID: 4cd45bf93f6d
Revises: d3161046d503
Create Date: 2024-11-13 12:18:59.936654

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '4cd45bf93f6d'
down_revision: Union[str, None] = 'd3161046d503'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('paymentinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('merchant_code', sqlmodel.sql.sqltypes.AutoString(length=191), nullable=True),
    sa.Column('pdt_token', sqlmodel.sql.sqltypes.AutoString(length=191), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_paymentinfo_user_id'), 'paymentinfo', ['user_id'], unique=False)
    op.create_table('productcolor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('color_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['color_id'], ['color.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_productcolor_color_id'), 'productcolor', ['color_id'], unique=False)
    op.create_index(op.f('ix_productcolor_product_id'), 'productcolor', ['product_id'], unique=False)
    op.create_table('productimage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('package_id', sa.Integer(), nullable=True),
    sa.Column('image_public_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('image_version', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['package_id'], ['specialpackage.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_productimage_package_id'), 'productimage', ['package_id'], unique=False)
    op.create_index(op.f('ix_productimage_product_id'), 'productimage', ['product_id'], unique=False)
    op.create_table('productsize',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('size', sqlmodel.sql.sqltypes.AutoString(length=191), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_productsize_product_id'), 'productsize', ['product_id'], unique=False)
    op.create_table('productreview',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('review_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['review_id'], ['review.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_productreview_product_id'), 'productreview', ['product_id'], unique=False)
    op.create_index(op.f('ix_productreview_review_id'), 'productreview', ['review_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_productreview_review_id'), table_name='productreview')
    op.drop_index(op.f('ix_productreview_product_id'), table_name='productreview')
    op.drop_table('productreview')
    op.drop_index(op.f('ix_productsize_product_id'), table_name='productsize')
    op.drop_table('productsize')
    op.drop_index(op.f('ix_productimage_product_id'), table_name='productimage')
    op.drop_index(op.f('ix_productimage_package_id'), table_name='productimage')
    op.drop_table('productimage')
    op.drop_index(op.f('ix_productcolor_product_id'), table_name='productcolor')
    op.drop_index(op.f('ix_productcolor_color_id'), table_name='productcolor')
    op.drop_table('productcolor')
    op.drop_index(op.f('ix_paymentinfo_user_id'), table_name='paymentinfo')
    op.drop_table('paymentinfo')
    # ### end Alembic commands ###
