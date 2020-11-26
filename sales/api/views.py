from rest_framework.views import APIView
from django.http.response import JsonResponse
from .queries import *


class AddAccount(APIView):
    def post(self, request):
        data = request.data
        try:
            insert_clause("""
                INSERT INTO py_cms.kadrlar
                    (ism, familiya, yil, telefon, mail)
                VALUES
                    ('{}','{}','{}','{}','{}')
            """.format(data['ism'], data['familiya'], data['yil'], data['telefon'], data['mail']))
            return JsonResponse('ADD', safe=False)
        except Exception as err:
            print(err)
            return JsonResponse('CANNOT ADD', safe=False)


class UpdateAccount(APIView):
    def put(self, request):
        data = request.data

        update_clause("""
            UPDATE py_cms.kadrlar
            SET
                ism = '{}',
                familiya = '{}',
                yil = '{}',
                telefon = '{}',
                mail = '{}'
            WHERE
                id = {}
        """.format(data['ism'], data['familiya'], data['yil'], data['telefon'], data['mail'], data['id']))
        return JsonResponse('UPDATE', safe=False)


class DeleteAccount(APIView):
    def delete(self, request):
        delete_clause("""
            DELETE FROM py_cms.kadrlar
            WHERE id = {}
        """.format(request.data['id']))
        return JsonResponse('DELETE', safe=False)


class AddPosition(APIView):
    def post(self, request):
        data = request.data
        try:
            insert_clause("""
                        INSERT INTO py_cms.lavozimlar
                            (lavozim, maosh_koef, ustama_id)
                        VALUES
                            ('{}','{}',{})
                    """.format(data['lavozim'], data['koef'] , data['ustama_id']))
            return JsonResponse('ADD', safe=False)
        except Exception as err:
            print(err)
            return JsonResponse('CANNOT ADD', safe=False)


class UpdatePosition(APIView):
    def put(self, request):
        data = request.data
        update_clause("""
                    UPDATE py_cms.lavozimlar
                    SET
                        lavozim = '{}',
                        maosh_koef = '{}',
                        ustama_id = {}
                    WHERE
                        id = {}
                """.format(data['lavozim'], data['koef'] , data['ustama_id'], data['id']))
        return JsonResponse('UPDATE', safe=False)


class DeletePosition(APIView):
    def delete(self, request):
        delete_clause("""
                    DELETE FROM py_cms.lavozimlar
                    WHERE id = {}
                """.format(request.data['id']))
        return JsonResponse('DELETE', safe=False)


class AddExtra(APIView):
    def post(self, request):
        return JsonResponse('ADD', safe=False)


class UpdateExtra(APIView):
    def put(self, request):
        return JsonResponse('UPDATE', safe=False)


class DeleteExtra(APIView):
    def put(self, request):
        return JsonResponse('DELETE', safe=False)


class AddTransaction(APIView):
    def post(self, request):
        return JsonResponse('ADD', safe=False)


class UpdateTransaction(APIView):
    def put(self, request):
        return JsonResponse('UPDATE', safe=False)


class DeleteTransaction(APIView):
    def put(self, request):
        return JsonResponse('DELETE', safe=False)
