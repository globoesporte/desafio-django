enqueteApp
    .controller('votoController', ['$scope', '$http', 'urlApi','urlService', function ($scope, $http, urlApi, urlService) {
        $scope.enquete = {};
        $scope.itemSelecionado = undefined;
        $scope.url = urlApi();

        $scope.init = function(value) {
            
            $http.get(urlService.obterUrl(urlService.Urls.OBTER, value))
                .then(
                    function(response){

                        $scope.enquete.nome = response.data.nome;
                        $scope.enquete.descricao = response.data.descricao;
                        $scope.enquete.data_criacao = new Date(response.data.data_criacao);
                        $scope.enquete.valor = response.data.valor;
                        $scope.enquete.id = response.data.id;
                        $scope.enquete.enquete = response.data.enquete;
                        $scope.enquete.itens = response.data.itens;
                    }, 
                    function(response){
                        alert('Houve um erro ao carregar');
                    });

        }

        $scope.votar = function(enquete) 
        {
            if ($scope.itemSelecionado == undefined)
                {
                    alert('Selecione um item');
                    return false;
                }

            $scope.voto = {};

            $scope.voto.item =  $scope.itemSelecionado.id;

            $http.post(urlService.obterUrl(urlService.Urls.VOTAR), $scope.voto)
                 .then(function(response)
                 {
                    //urlService.redirecionar(urlService.Urls.ALL, enquete);
                 }, function(response)
                 {
                    alert('Houve um erro ao editar');
                 });
        }

        $scope.selectItem = function(item) {
            $scope.itemSelecionado = item;
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
        OBTER :  "enquete/{0}",
        VOTAR : "api/voto/"
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