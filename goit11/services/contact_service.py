from sqlalchemy.orm import Session
from repositories.contact_repository import (
    get_contact, get_contacts, create_contact, update_contact,
    delete_contact, search_contacts, get_upcoming_birthdays
)
from schemas.contact import ContactCreate, ContactUpdate

def create_new_contact(db: Session, contact: ContactCreate):
    return create_contact(db, contact)

def get_all_contacts(db: Session, skip: int, limit: int):
    return get_contacts(db, skip, limit)

def get_contact_by_id(db: Session, contact_id: int):
    return get_contact(db, contact_id)

def update_existing_contact(db: Session, contact_id: int, contact: ContactUpdate):
    return update_contact(db, contact_id, contact)

def delete_contact_by_id(db: Session, contact_id: int):
    return delete_contact(db, contact_id)

def search_contact_by_query(db: Session, query: str):
    return search_contacts(db, query)

def get_contacts_with_upcoming_birthdays(db: Session):
    return get_upcoming_birthdays(db)
