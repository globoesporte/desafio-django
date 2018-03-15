enqueteApp
    .controller('votoController', ['$scope', '$http', 'urlApi','urlService', function ($scope, $http, urlApi, urlService) {
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

    }]);

enqueteApp.service('urlService', urlService )    
urlService.$inject = ['urlApi'];

function urlService(urlApi) 
{
    var serv = this;
    serv.redirecionar = redirecionar;
    serv.obterUrl = obterUrl;

    serv.Urls = {
        // API
        LISTAR :  "item/?enquete={0}&format=json",
        VOTAR : "voto/"
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