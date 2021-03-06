// Copyright 2019 Polyaxon, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

/*
 * Polyaxon SDKs and REST API specification.
 * Polyaxon SDKs and REST API specification.
 *
 * OpenAPI spec version: 1.0.0
 * Contact: contact@polyaxon.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 2.4.10
 *
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['ApiClient', 'model/V1ArtifactMount', 'model/V1BuildContext', 'model/V1RepoInit'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('./V1ArtifactMount'), require('./V1BuildContext'), require('./V1RepoInit'));
  } else {
    // Browser globals (root is window)
    if (!root.PolyaxonSdk) {
      root.PolyaxonSdk = {};
    }
    root.PolyaxonSdk.V1Init = factory(root.PolyaxonSdk.ApiClient, root.PolyaxonSdk.V1ArtifactMount, root.PolyaxonSdk.V1BuildContext, root.PolyaxonSdk.V1RepoInit);
  }
}(this, function(ApiClient, V1ArtifactMount, V1BuildContext, V1RepoInit) {
  'use strict';

  /**
   * The V1Init model module.
   * @module model/V1Init
   * @version 1.0.0
   */

  /**
   * Constructs a new <code>V1Init</code>.
   * @alias module:model/V1Init
   * @class
   */
  var exports = function() {
  };

  /**
   * Constructs a <code>V1Init</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/V1Init} obj Optional instance to populate.
   * @return {module:model/V1Init} The populated <code>V1Init</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();
      if (data.hasOwnProperty('repos'))
        obj.repos = ApiClient.convertToType(data['repos'], [V1RepoInit]);
      if (data.hasOwnProperty('artifacts'))
        obj.artifacts = ApiClient.convertToType(data['artifacts'], [V1ArtifactMount]);
      if (data.hasOwnProperty('build'))
        obj.build = V1BuildContext.constructFromObject(data['build']);
    }
    return obj;
  }

  /**
   * @member {Array.<module:model/V1RepoInit>} repos
   */
  exports.prototype.repos = undefined;

  /**
   * @member {Array.<module:model/V1ArtifactMount>} artifacts
   */
  exports.prototype.artifacts = undefined;

  /**
   * @member {module:model/V1BuildContext} build
   */
  exports.prototype.build = undefined;

  return exports;

}));
