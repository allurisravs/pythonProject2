from flask import Flask, make_response, jsonify, request, redirect, url_for
from flask.views import MethodView
from flask import render_template
from RequiredData import *

app = Flask(__name__)


class DataApi(MethodView):


    def get(self):
        """ Return the all rows from csv file inventory collection """
        return make_response(jsonify(RequiredCsvData()), 200)



class DataAddressApi(MethodView):


    def get(self, addr):
        """ returns rows which matches the given address"""
        return make_response(jsonify(final_list=addressess(addr)), 200)

class DataAddressMaskApi(MethodView):


    def get(self, addr,mask):
        """ returns rows which are matched with address and mask """
        return make_response(jsonify(final_list=FinalData(addr,mask)), 200)

class DataReportAddressMaskApi(MethodView):
    def get(self, addr,mask):
        """returns in html table """
        return render_template("reports.html", reports=FinalData(addr,mask))



app.add_url_rule("/addressess", view_func=DataApi.as_view("data_api"))
app.add_url_rule("/addressess/<addr>", view_func=DataAddressApi.as_view("data_address_api"))
app.add_url_rule("/addressess/<addr>/<mask>", view_func=DataAddressMaskApi.as_view("data_address_mask_api"))
app.add_url_rule("/reports/<addr>/<mask>",view_func=DataReportAddressMaskApi.as_view("data_report_address_mask_api"))
if __name__ == "__main__":
    app.run()