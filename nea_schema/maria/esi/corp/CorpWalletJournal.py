from datetime import datetime as dt
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    BIGINT as BigInt, \
    BOOLEAN as Boolean, \
    DATETIME as DateTime, \
    DOUBLE as Double, \
    INTEGER as Integer, \
    TEXT as Text, \
    TINYINT as TinyInt, \
    TINYTEXT as TinyText

from ...Base import Base

class CorpWalletJournal(Base):    
    __tablename__ = 'corp_WalletJournal'
    
    ## Columns
    record_time = Column(DateTime)
    amount = Column(Double(unsigned=False))
    balance = Column(Double(unsigned=True))
    context_id = Column(BigInt(unsigned=True))
    context_id_type = Column(TinyText)
    date = Column(DateTime)
    description = Column(Text)
    division = Column(TinyInt(unsigned=True))
    first_party_id = Column(BigInt(unsigned=True))
    journal_id = Column(BigInt(unsigned=True), primary_key=True, autoincrement=False)
    reason = Column(Text)
    ref_type = Column(TinyText)
    second_party_id = Column(BigInt(unsigned=True))
    tax = Column(Double(unsigned=True))
    tax_receiver_id = Column(BigInt(unsigned=True))
    
    ## Relationships
    transaction = relationship(
        'CorpWalletTransaction',
        primaryjoin='CorpWalletJournal.journal_id == foreign(CorpWalletTransaction.journal_ref_id)',
        viewonly=True, uselist=False,
    )

    @classmethod
    def esi_parse(cls, esi_return, orm=True):
        record_time = dt.strptime(esi_return.headers.get('Last-Modified'), '%a, %d %b %Y %H:%M:%S %Z')
        division = esi_return.url.split('/')[7]
        record_items = [{
            'record_time': record_time,
            'journal_id': row.pop('id'),
            **row,
            'date': dt.strptime(row.get('date'), '%Y-%m-%dT%H:%M:%SZ'),
            'division': division,
        } for row in esi_return.json()]
        if orm: record_items = [cls(**row) for row in record_items]
        return record_items
