from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.drop_down_stocks.items = anvil.server.call('getTickers')
    
    # Any code you write here will run when the form opens.

  def drop_down_stocks_change(self, **event_args):
    """This method is called when an item is selected"""
    #alert('You selected a stock ' + self.drop_down_stocks.selected_value)
    ticker = self.drop_down_stocks.selected_value
    self.stockTicker.text = ticker
    self.stockPrice.text = anvil.server.call('getPrice', ticker)

  def drop_down_stocks_show(self, **event_args):
    """This method is called when the DropDown is shown on the screen"""
    ticker = self.drop_down_stocks.selected_value
    self.stockTicker.text = ticker
    self.stockPrice.text = anvil.server.call('getPrice', ticker)


