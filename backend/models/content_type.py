from sqlalchemy import create_engine, Column, Integer, String, Date, Time, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import csv

Base = declarative_base()

class ContentTypeChartData(Base):
    __tablename__ = 'content_type_chart_data'

    date = Column(Date, primary_key=True)
    content_type = Column(String, primary_key=True)
    views = Column(Integer)

class ContentTypeTableData(Base):
    __tablename__ = 'content_type_table_data'

    content_type = Column(String, primary_key=True)
    views = Column(Integer)
    watch_time = Column(Float)
    average_view_duration = Column(Time)

class ContentTypeTotals(Base):
    __tablename__ = 'content_type_totals'

    date = Column(Date, primary_key=True)
    views = Column(Integer)

# Define your database connection
engine = create_engine('sqlite:///content_type_data.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Read and insert data from CSV files
csv_files = {
    'ContentTypeChartData.csv': ContentTypeChartData,
    'ContentTypeTableData.csv': ContentTypeTableData,
    'ContentTypeTotals.csv': ContentTypeTotals
}

for file, model in csv_files.items():
    with open(file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            session.add(model(**row))

session.commit()
