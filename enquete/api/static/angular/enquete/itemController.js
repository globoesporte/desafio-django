enqueteApp
    .controller('itemEditController', ['$scope', '$http', 'urlApi','urlService', function ($scope, $http, urlApi, urlService) {
        $scope.item = {};
        $scope.url = urlApi();
        
        $scope.init = function(value) {
            
            $http.get(urlService.obterUrl(urlService.Urls.OBTER, value))
                .then(
                    function(response){

                        $scope.item.nome = response.data.nome;
                        $scope.item.descricao = response.data.descricao;
                        $scope.item.data_criacao = new Date(response.data.data_criacao);
                        $scope.item.valor = response.data.valor;
                        $scope.item.id = response.data.id;
                        $scope.item.enquete = response.data.enquete;

                        console.log(response.data);
                    }, 
                    function(response){
                        alert('Houve um erro ao carregar');
                    });

        }

        $scope.editar = function()
        {
            console.log(urlService.obterUrl(urlService.Urls.EDITAR, $scope.item.id))
           $http.put(urlService.obterUrl(urlService.Urls.EDITAR, $scope.item.id), $scope.item)
                 .then(function(response)
                 {
                    urlService.redirecionar(urlService.Urls.ALL, $scope.item.enquete);

                 }, function(response){
                    alert('Houve um erro ao editar');
                 });
        }

        $scope.incluir = function(enquete) 
        {
            $scope.item.enquete = enquete;
            $http.post(urlService.obterUrl(urlService.Urls.INCLUIR), $scope.item)
                 .then(function(response)
                 {
                    urlService.redirecionar(urlService.Urls.ALL, enquete);
                 }, function(response)
                 {
                    alert('Houve um erro ao editar');
                 });
        }

        $scope.excluir = function(obj)
        {
            $http.delete(urlService.obterUrl(urlService.Urls.EXCLUIR, obj.e.id), $scope.item)
                 .then(function(response)
                 {
                    urlService.redirecionar(urlService.Urls.ALL, obj.e.id);

                 }, function(response)
                 {
                    alert('Houve um erro ao excluir');
                 });
        }

        $scope.obterTodos = function(value) 
        {
            $scope.data = {};
            $scope.item.id = value;
            $http.get(urlService.obterUrl(urlService.Urls.LISTAR, value))
                 .then(function(response)
                 {
                    $scope.items = []; //inicializa

                     if (!response.data) {
                         return false;
                     }

                      response.data.forEach(element => {
                          var e ={
                              nome : element.nome,
                              descricao : element.descricao,
                              data_criacao : new Date(element.data_criacao),
                              id :  element.id,
                              valor : element.valor
                          };

                          $scope.items.push(e);

                      }); 
                 }, function()
                 {
                    alert('Houve um erro ao obter Todos');
                 });
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
        ALL :     "item/all/?enquete={0}",
        NEW :     "item/new",
        EDIT :    "item/edit/{0}",

        // API
        LISTAR :  "item/?enquete={0}&format=json",
        OBTER :   "item/{0}/?format=json",
        EDITAR :  "item/{0}/",
        INCLUIR : "item/",
        EXCLUIR : "item/{0}/"
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