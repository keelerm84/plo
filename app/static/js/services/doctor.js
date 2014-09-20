'use strict';

angular.module('plo')
  .factory('Doctor', ['$resource', function ($resource) {
    return $resource('plo/doctors/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
