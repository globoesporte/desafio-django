var enqueteApp = angular.module('enqueteApp', ['ngCookies']);
/**
 * @ngdoc controller
 * @name adminApp.controller:enquete
 * @function
 * @description
 * # enquete
 */

 
enqueteApp
    .controller('enqueteEditController', ['$scope', '$http', 'urlApi','urlService', function ($scope, $http, urlApi, urlService) {
        $scope.enquete = {};
        $scope.url = urlApi();
        
        $scope.init = function(value) {
            
            $scope.enquete.id = value;

            $http.get(urlService.obterUrl(urlService.Urls.OBTER, value))
                .then(
                    function(response){

                        $scope.enquete.nome = response.data.nome;
                        $scope.enquete.descricao = response.data.descricao;
                        $scope.enquete.data_criacao = new Date(response.data.data_criacao);
                        
                    }, 
                    function(response){
                        alert('Houve um erro ao carregar');
                    });

        }

        $scope.editar = function() 
        {
            $http.put(urlService.obterUrl(urlService.Urls.EDITAR, $scope.enquete.id), $scope.enquete)
                 .then(function(response)
                 {
                    urlService.redirecionar(urlService.Urls.ALL);

                 }, function(response)
                 {
                    alert('Houve um erro ao editar');
                 });
        }

        $scope.incluir = function() 
        {
            $http.post(urlService.obterUrl(urlService.Urls.INCLUIR), $scope.enquete)
                 .then(function(response)
                 {
                    urlService.redirecionar(urlService.Urls.ALL);

                 }, function(response)
                 {
                    alert('Houve um erro ao editar');
                 });
        }

        $scope.excluir = function(obj)
        {
            console.log(obj);
            $http.delete(urlService.obterUrl(urlService.Urls.EXCLUIR, obj.e.id), $scope.enquete)
                 .then(function(response)
                 {
                    urlService.redirecionar(urlService.Urls.ALL);

                 }, function(response)
                 {
                    alert('Houve um erro ao excluir');
                 });
        }

        $scope.obterTodos = function() 
        {
            $scope.data = {};

            $http.get(urlService.obterUrl(urlService.Urls.LISTAR))
                 .then(function(response)
                 {
                    $scope.enquetes = []; //inicializa

                     if (!response.data) {
                         return false;
                     }

                      response.data.forEach(element => {
                          var e ={
                              nome : element.nome,
                              descricao : element.descricao,
                              data_criacao : new Date(element.data_criacao),
                              id :  element.id,
                              itens : element.itens
                          };

                          $scope.enquetes.push(e);

                      }); 
                 }, function()
                 {
                    alert('Houve um erro ao obter Todos');
                 });
        }

        $scope.openModal = function(id) {
            ModalService.Open(id);
        }
 
        $scope.closeModal = function(id){
            ModalService.Close(id);
        }

    }]);

enqueteApp.factory('urlApi', ['$window', function(win) {
    
    return function() {
        return  window.origin + '/';
      }
    }
]);


enqueteApp.service('urlService', urlService )    
urlService.$inject = ['urlApi'];

function urlService(urlApi) 
{
    var serv = this;
    serv.redirecionar = redirecionar;
    serv.obterUrl = obterUrl;

    serv.Urls = {
        // VIEW
        ALL :     "enquete/all",
        NEW :     "enquete/new",
        EDIT :    "enquete/edit/{0}",

        // API
        LISTAR :  "enquete/?format=json",
        OBTER :   "enquete/{0}",
        EDITAR :  "enquete/{0}/",
        INCLUIR : "enquete/",
        EXCLUIR : "enquete/{0}/"
    }

    function redirecionar(url, value)
    {
        if(value != undefined)        
            window.location = urlApi() + url.toString().replace('{0}', value);
        else
            window.location = urlApi() + url.toString();
    }

    function obterUrl(urlType, value)
    {
        var url = urlApi() + urlType.toString();
        
        if(value != undefined) 
            return url.replace('{0}', value);
        
        return url;
    }
}

enqueteApp.config(['$httpProvider','$interpolateProvider', function($httpProvider, $interpolateProvider) {
        
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
        $httpProvider.defaults.withCredentials = true;
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }]).
    run(['$http','$cookies', function($http, $cookies) {
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    }]);
   