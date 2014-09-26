'use strict';

angular.module('plo')
  .factory('Resource', ['$resource', function ($resource) {
    return $resource('plo/resources/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
