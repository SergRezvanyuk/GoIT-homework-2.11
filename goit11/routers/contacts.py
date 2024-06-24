from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.contact import Contact, ContactCreate, ContactUpdate
from services.contact_service import (
    create_new_contact, get_all_contacts, get_contact_by_id, update_existing_contact,
    delete_contact_by_id, search_contact_by_query, get_contacts_with_upcoming_birthdays
)
from dependencies.database import get_db

router = APIRouter()

@router.post("/contacts/", response_model=Contact)
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    return create_new_contact(db, contact)

@router.get("/contacts/", response_model=List[Contact])
def read_contacts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_all_contacts(db, skip, limit)

@router.get("/contacts/{contact_id}", response_model=Contact)
def read_contact(contact_id: int, db: Session = Depends(get_db)):
    db_contact = get_contact_by_id(db, contact_id)
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact

@router.put("/contacts/{contact_id}", response_model=Contact)
def update_contact(contact_id: int, contact: ContactUpdate, db: Session = Depends(get_db)):
    return update_existing_contact(db, contact_id, contact)

@router.delete("/contacts/{contact_id}", response_model=Contact)
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    return delete_contact_by_id(db, contact_id)

@router.get("/contacts/search/", response_model=List[Contact])
def search_contacts(query: str, db: Session = Depends(get_db)):
    return search_contact_by_query(db, query)

@router.get("/contacts/upcoming-birthdays/", response_model=List[Contact])
def upcoming_birthdays(db: Session = Depends(get_db)):
    return get_contacts_with_upcoming_birthdays(db)
