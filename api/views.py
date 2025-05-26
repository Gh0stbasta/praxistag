from django.shortcuts import render
from .models import products
from rest_framework.generics import ListAPIView
from .serializer import ProductSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListCreateAPIView



class ProductListView(ListCreateAPIView):
    """
    ProductListView stellt eine API-Ansicht bereit, die eine Liste aller Produkte zurückgibt
    und das Erstellen neuer Produkte ermöglicht.

    Die zurückgegebenen Produktdaten enthalten folgende Felder:
        - name: Name des Produkts
        - short_description: Kurzbeschreibung des Produkts
        - product_description: Ausführliche Produktbeschreibung
        - stock: Lagerbestand des Produkts
        - price: Preis des Produkts

    Verwendet das ProductSerializer, um die Produktdaten zu serialisieren.
    """
    queryset = products.objects.all()
    serializer_class = ProductSerializer

class ProductCreateView(CreateAPIView):
    """
    ProductCreateView ermöglicht das Erstellen neuer Produktinstanzen über eine API.

    Die zu erstellenden Produktdaten müssen folgende Felder enthalten:
        - name: Name des Produkts
        - short_description: Kurzbeschreibung des Produkts
        - product_description: Ausführliche Produktbeschreibung
        - stock: Lagerbestand des Produkts
        - price: Preis des Produkts

    Diese View verwendet das ProductSerializer, um die Validierung und Serialisierung der Produktdaten sicherzustellen.
    Sie stellt eine POST-Methode bereit, mit der neue Produkte in der Datenbank angelegt werden können.
    """
    queryset = products.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    """
    ProductDetailView ermöglicht das Abrufen, Aktualisieren und Löschen einzelner Produktinstanzen.

    Die Produktdaten enthalten folgende Felder:
        - name: Name des Produkts
        - short_description: Kurzbeschreibung des Produkts
        - product_description: Ausführliche Produktbeschreibung
        - stock: Lagerbestand des Produkts
        - price: Preis des Produkts

    Diese View verwendet das RetrieveUpdateDestroyAPIView-Generic von Django REST Framework,
    um die HTTP-Methoden GET, PUT, PATCH und DELETE für Produkte bereitzustellen.

    Attribute:
        queryset (QuerySet): Die vollständige Liste aller Produktobjekte.
        serializer_class (Serializer): Serializer-Klasse zur Umwandlung von Produktdaten.

    Verwendung:
        - GET: Gibt die Details eines Produkts zurück.
        - PUT/PATCH: Aktualisiert die Felder name, short_description, product_description, stock, price eines Produkts.
        - DELETE: Löscht ein Produkt.
    """
    queryset = products.objects.all()
    serializer_class = ProductSerializer
