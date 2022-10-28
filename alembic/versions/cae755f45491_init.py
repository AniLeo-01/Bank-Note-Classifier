"""init

Revision ID: cae755f45491
Revises: 
Create Date: 2022-10-24 10:42:52.362766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cae755f45491'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "predictions",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("prediction_label", sa.String, nullable=False),
        sa.Column("prediction_score", sa.Float, nullable=False)
    )


def downgrade():
    op.drop_table("predictions")
