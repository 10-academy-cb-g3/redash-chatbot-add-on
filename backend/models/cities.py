from sqlalchemy import create_engine, Column, Integer, String, Date, Time, Float
from sqlalchemy.ext.declarative import declarative_base

# Define the Base class for declarative class definitions
Base = declarative_base()

# Define class for cities_chart_data table
class CitiesChartData(Base):
    __tablename__ = 'cities_chart_data'

    # Define columns
    date = Column(Date, primary_key=True)
    cities = Column(String, primary_key=True)
    city_name = Column(String)
    views = Column(Integer)

# Define class for cities_table_data table
class CitiesTableData(Base):
    __tablename__ = 'cities_table_data'

    # Define columns
    cities = Column(String, primary_key=True)
    city_name = Column(String, primary_key=True)
    geography1 = Column(String)
    geography2 = Column(String)
    views = Column(Integer)
    watch_time = Column(Float)
    average_view_duration = Column(Time)

# Define class for cities_totals table
class CitiesTotals(Base):
    __tablename__ = 'cities_totals'

    # Define columns
    date = Column(Date, primary_key=True)
    views = Column(Integer)
