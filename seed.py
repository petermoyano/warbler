"""Seed database with sample data from CSV Files."""

from csv import DictReader
from app import db
from models import User, Message, Follows, Likes


db.drop_all()
db.create_all()

with open('generator/users.csv') as users:
    db.session.bulk_insert_mappings(User, DictReader(users))

with open('generator/messages.csv') as messages:
    db.session.bulk_insert_mappings(Message, DictReader(messages))

with open('generator/follows.csv') as follows:
    db.session.bulk_insert_mappings(Follows, DictReader(follows))

db.session.commit()

def seed_likes():
    """Seed some likes ment for testing"""
    l1 = Likes(user_id=189, message_id=1)
    l2 = Likes(user_id=189, message_id=2)
    l3 = Likes(user_id=1, message_id=45)
    l4 = Likes(user_id=1, message_id=67)
    l5 = Likes(user_id=2, message_id=89)
    db.session.add_all([l1, l2, l3, l4, l5])
    db.session.commit()

seed_likes()
