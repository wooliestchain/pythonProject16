from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from ventes import add_sale_to_database
from recette import get_quantity_by_product, get_quantity_by_product_a_month, get_recete_by_product, get_recete_by_product_a_month, get_recete_of_day,\
    get_recete_of_day_by_product, get_recete_of_month_by_product, get_product_stuf
from ventes import get_sales_by_product, get_total_sales_by_month_for_all_product, get_total_sales_by_month_for_a_product
from datetime import datetime
from produit import add_product, modify_product
from commerce import add_commerce, modify_commerce
from no_entry import no_entry_max_month_of_sales, no_entry_max_day_of_sales, no_entry_get_quantity_by_product, total_recette, mvp_recette,\
    no_entry_max_month, no_entry_max_sales
from tkinter import messagebox



now = datetime.now()
year = now.year
month = now.month
day = now.day

class HelloWorldService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def say_hello(ctx, name):
        return "Hello, %s!" % name

#Classe pour gérer les ventes
class SaleService(ServiceBase):
    @rpc(Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, _returns=Unicode)
    def add_sale(ctx, produit, montant, quantite, now = datetime.now(), year = now.year, month = now.month, day = now.day ):
        add_sale_to_database(produit, montant, quantite, now, year, month, day)
        return "Vente ajoutée avec succès !"

#obtenir le nombre de vente pour un produit
    @rpc(Unicode, _returns=Unicode)
    def get_sale(ctx, produit):
        try:
            sales = get_sales_by_product(produit)
            nb_ventes = str(sales)
        except ValueError:
            nb_ventes = "0"
        return nb_ventes

#Obtenir la quantité vendue pour un produit
    @rpc(Unicode, _returns=Unicode)
    def get_qt(ctx, produit):
        try:
            sales = get_quantity_by_product(produit)
            nb_ventes = str(sales)
        except ValueError:
            nb_ventes = "0"
        return nb_ventes

        # Obtenir la quantité vendue pour un produit durant un mois
    @rpc(Unicode, Unicode, _returns=Unicode)
    def get_qt_month(ctx, produit, mois):
        try:
            sales = get_quantity_by_product_a_month(produit, mois)
            nb_ventes = str(sales)
        except ValueError:
            nb_ventes = "0"
        return nb_ventes

    @rpc(Unicode, _returns=Unicode)
    def product_infos(ctx, produit):
        try:
            result = get_product_stuf(produit)
            message = f"Nom du produit : {result[0][0]}\nTotal des ventes : {result[0][1]}\nNombre de ventes : {result[0][2]}\nTotal des quantités vendues : {result[0][3]}"
            return message
        except ValueError as e:
            return str(e)

    @rpc(Unicode, _returns=Unicode)
    def product_infos_name(ctx, produit):
        try:
            result = get_product_stuf(produit)
            message = f"{result[0][0]}"
            return message
        except ValueError as e:
            return str(e)

    @rpc(Unicode, _returns=Unicode)
    def product_infos_vt(ctx, produit):
        try:
            result = get_product_stuf(produit)
            message = f"{result[0][1]}"
            return message
        except ValueError as e:
            return str(e)

    @rpc(Unicode, _returns=Unicode)
    def product_infos_nbventes(ctx, produit):
        try:
            result = get_product_stuf(produit)
            message = f"{result[0][2]}"
            return message
        except ValueError as e:
            return str(e)

    @rpc(Unicode, _returns=Unicode)
    def product_infos_qtventes(ctx, produit):
        try:
            result = get_product_stuf(produit)
            message = f"{result[0][3]}"
            return message
        except ValueError as e:
            return str(e)

    #obtenir le nombre de ventes pour un mois
    @rpc(Unicode, _returns=Unicode)
    def all_month_sales(ctx, mois):
        try:
            sales = get_total_sales_by_month_for_all_product(mois)
            nb_ventes = str(sales)
        except ValueError:
            nb_ventes = "0"
        return nb_ventes

#Obtenir le nombre de ventes pour un produit au cours d'un mois
    @rpc(Unicode, Unicode, _returns=Unicode)
    def all_month_sales_one_product(ctx,produit, mois):
        try:
            sales = get_total_sales_by_month_for_a_product(produit,mois)
            nb_ventes = str(sales)
        except ValueError:
            nb_ventes = "0"
        return nb_ventes

    #recette d'un produit
    @rpc(Unicode, _returns=Unicode)
    def recette_a_product(ctx, produit):
        try:
            rec = get_recete_by_product(produit)
            total_rec = str(rec)
        except ValueError:
            total_rec = "0"
        return total_rec
    #recette d'un produit sur un mois
    @rpc(Unicode, Unicode, _returns=Unicode)
    def recette_a_product_a_month(ctx, produit, mois):
        try:
            rec = get_recete_by_product_a_month(produit, mois)
            total_rec = str(rec)
        except ValueError:
            total_rec = "0"
        return total_rec

    #recette pour le jour en cours
    @rpc(Unicode, _returns=Unicode)
    def recette_a_day(ctx, date):
        try:
            rec = get_recete_of_day(date)
            total_rec = str(rec)
        except ValueError:
            total_rec = "0"
        return total_rec

    # recette pour le jour en cours pour un produit
    @rpc(Unicode, Unicode, _returns=Unicode)
    def recette_of_day_for_product(ctx, produit, day=now.day):
        try:
            rec = get_recete_of_day_by_product(produit,day)
            total_rec = str(rec)
        except ValueError:
            total_rec = "0"
        return total_rec


class NoEntry(ServiceBase):
    #Le mois avec les recettes les plus élévées
    @rpc(_returns=Unicode)
    def get_max_month_sales(ctx):
        rows = no_entry_max_month_of_sales()
        max_month_sales = f"Mois: {rows[0][0]}, Ventes Max: {rows[0][1]}"
        return max_month_sales

    @rpc(_returns=Unicode)
    def max_month(ctx):
        rows = no_entry_max_month()
        #max_month = f"Le mois le plus lucratif: {rows[0][0]} ème mois"
        if rows[0][0] == 4:
            max_month = f"Avril"

        if rows[0][0] == 1:
            max_month = f"Le mois le plus lucratif est le mois de Janvier"

        if rows[0][0] == 2:
            max_month = f"Le mois le plus lucratif est le mois de Février "

        if rows[0][0] == 3:
            max_month = f"Le mois le plus lucratif est le moi de Mars"

        if rows[0][0] == 5:
            max_month = f"Le mois le plus lucratif est le moi de Mai"

        if rows[0][0] == 6:
            max_month = f"Le mois le plus lucratif est le moi de Juin"

        if rows[0][0] == 7:
            max_month = f"Le mois le plus lucratif est le moi de Juillet"

        if rows[0][0] == 8:
            max_month = f"Le mois le plus lucratif est le mois d'Août"

        if rows[0][0] == 9:
            max_month = f"Le mois le plus lucratif est le mois de Septembre"

        if rows[0][0] == 10:
            max_month = f"Le mois le plus lucratif est le mois d'Octobre"

        if rows[0][0] == 11:
            max_month = f"Le mois le plus lucratif est le mois de Novembre"

        if rows [0][0] == 12:
            max_month = f"Le mois le plus lucratif est le mois de Décembre"
        return max_month

    @rpc(_returns=Unicode)
    def max_month_sales(ctx):
        rows = no_entry_max_sales()
        max_month = f"{rows[0][1]}"
        return max_month

    #La date avec les recettes les plus élévées
    @rpc(_returns=Unicode)
    def get_max_date_sales(ctx):
        rows = no_entry_max_day_of_sales()
        max_month_sales = f"{rows[0][0]}"
        return max_month_sales

    # La date avec les recettes les plus élévées
    @rpc(_returns=Unicode)
    def get_max_date_sales_vt(ctx):
        rows = no_entry_max_day_of_sales()
        max_month_sales = f"{rows[0][1]}"
        return max_month_sales

    #Le total des recettes
    @rpc(_returns=Unicode)
    def total_rec(ctx):
        rows = total_recette()
        max_month_sales = f"{rows[0][0]}"
        return max_month_sales


    #Le produit qui a généré le plus de recette
    @rpc(_returns=Unicode)
    def mvp_recette_service(ctx):
        try:
            result = mvp_recette()
            message = f"{result[0][0]}"
            return message
        except ValueError as e:
            return str(e)

    @rpc(_returns=Unicode)
    def mvp_recette_service_qt(ctx):
        try:
            result = mvp_recette()
            message = f"{result[0][1]}"
            return message
        except ValueError as e:
            return str(e)

    @rpc(_returns=Unicode)
    def mvp_recette_service_vt(ctx):
        try:
            result = mvp_recette()
            message = f"{result[0][2]}"
            return message
        except ValueError as e:
            return str(e)


class ProductService(ServiceBase):

    @rpc(Unicode, Unicode, Unicode, Unicode, _returns=Unicode)
    def new_product(ctx, code, produit, cat, prix):
        add_product(code, produit, cat, prix)
        return "Produit ajouté avec succès"

    @rpc(Unicode, Unicode, Unicode, Unicode, _returns=Unicode)
    def mod_product(ctx, code, new_prod, new_cat, new_prix):
        modify_product(code, new_prod, new_cat, new_prix)
        return "Produit modifié avec succès"


class CommerceService(ServiceBase):

    @rpc(Unicode, Unicode, Unicode, Unicode, Unicode, _returns=Unicode)
    def new_commerce(ctx, code, nom, year, sector, descr):
        add_commerce(code, nom, year, sector, descr)
        #success = messagebox.showinfo('Infos', 'Infos stored')
        return "Votre commerce a été ajoutée"

    @rpc(Unicode, Unicode, Unicode, Unicode, _returns=Unicode)
    def mod_commerce(ctx, code, new_name, new_sector, new_descr):
        modify_commerce(code, new_name, new_sector, new_descr)
        return "Commerce modifié avec succès"

application = Application([HelloWorldService, SaleService, NoEntry, ProductService, CommerceService], tns='http://example.com/hello', in_protocol=Soap11(), out_protocol=Soap11())

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    wsgi_app = WsgiApplication(application)
    server = make_server('localhost', 8000, wsgi_app)
    server.serve_forever()
