from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text, Index, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

Base = declarative_base()

class MessageDirection(enum.Enum):
    INBOUND = "inbound"
    OUTBOUND = "outbound"

class Corpus(Base):
    __tablename__ = 'corpora'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(Text)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    passages = relationship("Passage", back_populates="corpus")

class Passage(Base):
    __tablename__ = 'passages'
    
    id = Column(Integer, primary_key=True)
    corpus_id = Column(Integer, ForeignKey('corpora.id'), nullable=False)
    title = Column(String(255))
    content = Column(Text, nullable=False)
    chapter = Column(Integer)
    verse = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    corpus = relationship("Corpus", back_populates="passages")

    __table_args__ = (
        Index('idx_passage_chapter_verse', 'corpus_id', 'chapter', 'verse'),
    )

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    phone_number = Column(String(20), nullable=False, unique=True)
    is_active = Column(Boolean, default=True)
    timezone = Column(String(50), default='UTC')
    preferred_corpus_id = Column(Integer, ForeignKey('corpora.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    last_message_sent = Column(DateTime)
    last_interaction = Column(DateTime)
    message_count = Column(Integer, default=0)
    preferred_send_time = Column(String(5), default='09:00')  # Format: HH:MM
    
    preferred_corpus = relationship("Corpus")
    sessions = relationship("Session", back_populates="user")

class Session(Base):
    __tablename__ = 'sessions'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime)
    is_active = Column(Boolean, default=True)
    
    user = relationship("User", back_populates="sessions")
    messages = relationship("Message", back_populates="session")

class Message(Base):
    __tablename__ = 'messages'
    
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey('sessions.id'), nullable=False)
    direction = Column(Enum(MessageDirection), nullable=False)
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    passage_id = Column(Integer, ForeignKey('passages.id'))
    status = Column(String(20), default='sent')  # sent, delivered, failed
    error_message = Column(Text)
    twilio_message_id = Column(String(50))
    
    session = relationship("Session", back_populates="messages")
    passage = relationship("Passage")
    
    __table_args__ = (
        Index('idx_message_session_time', 'session_id', 'timestamp'),
    )
