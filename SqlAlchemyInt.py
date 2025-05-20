import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP, JSON, UUID
from datetime import datetime
import uuid

# db = sa.create_engine("sqlite:///:memory:")
db = sa.create_engine("postgresql://tjsim:simadmin@192.168.0.183/tjsim")
Session = sessionmaker(bind=db)
Base = declarative_base()


class ComRecord(Base):
    __tablename__ = 'com_record'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date_time = Column(TIMESTAMP)
    trans_id = Column(UUID)
    retrieval_reference_number = Column(String(12))
    msgtype = Column(String(3))
    direction = Column(Integer)
    response_code = Column(String(3))
    amount = Column(Integer)
    card_acceptor = Column(String(15))
    terminal = Column(String(8))
    message_body = Column(JSON)

def __repr__(self) -> str:
        return (f"ComRecord(id={self.id}, date_time={self.date_time}, trans_id={self.trans_id}, "
                f"retrieval_reference_number='{self.retrieval_reference_number}', msgtype='{self.msgtype}', "
                f"direction={self.direction}, response_code='{self.response_code}', amount={self.amount}, "
                f"card_acceptor='{self.card_acceptor}', terminal='{self.terminal}', message_body={self.message_body})")


def create_tran_record_request(data) -> None:
    Base.metadata.create_all(db)

    new_record = ComRecord(
    date_time=datetime.now(),
    trans_id=data['reference'],
    # retrieval_reference_number="123456789012",
    msgtype="200",
    direction=1,
    # response_code="00",
    amount=data['amount'],
    card_acceptor=data['store'],
    terminal=data['pos'],
    message_body=data
)

    with Session() as session:
        session.add(new_record)
        session.commit()
        # print(session.query(new_record).all())

def create_tran_record_response(data) -> None:
    Base.metadata.create_all(db)

    new_record = ComRecord(
    date_time=datetime.now(),
    trans_id=data['reference'],
    retrieval_reference_number=data['rrn'],
    msgtype="210",
    direction=2,
    response_code=data["response_code"],
    amount=data['amount'],
    card_acceptor=data['store'],
    terminal=data['pos'],
    message_body=data
)

    with Session() as session:
        session.add(new_record)
        session.commit()
        # print(session.query(new_record).all())

if __name__ == "__main__":
    create_tran_record_request()


    # new_record = ComRecord(
    # date_time=datetime.now(),
    # trans_id=str(uuid.uuid4()),
    # retrieval_reference_number="123456789012",
    # msgtype="200",
    # direction=1,
    # response_code="00",
    # amount=1000,
    # card_acceptor="Shop123",
    # terminal="ATM001",
    # message_body={"status": "approved", "details": "Transaction successful"}