/**
 * CrowdLabelAPI
 * API for CrowdLabel
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Corners from './Corners';

/**
 * The BoundingBoxAnswer model module.
 * @module model/BoundingBoxAnswer
 * @version 0.1.0
 */
class BoundingBoxAnswer {
    /**
     * Constructs a new <code>BoundingBoxAnswer</code>.
     * @alias module:model/BoundingBoxAnswer
     * @param boxes {Array.<module:model/Corners>} 
     */
    constructor(boxes) { 
        
        BoundingBoxAnswer.initialize(this, boxes);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, boxes) { 
        obj['boxes'] = boxes;
    }

    /**
     * Constructs a <code>BoundingBoxAnswer</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BoundingBoxAnswer} obj Optional instance to populate.
     * @return {module:model/BoundingBoxAnswer} The populated <code>BoundingBoxAnswer</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BoundingBoxAnswer();

            if (data.hasOwnProperty('boxes')) {
                obj['boxes'] = ApiClient.convertToType(data['boxes'], [Corners]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BoundingBoxAnswer</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BoundingBoxAnswer</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of BoundingBoxAnswer.RequiredProperties) {
            if (!data[property]) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['boxes']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['boxes'])) {
                throw new Error("Expected the field `boxes` to be an array in the JSON data but got " + data['boxes']);
            }
            // validate the optional field `boxes` (array)
            for (const item of data['boxes']) {
                Corners.validateJsonObject(item);
            };
        }

        return true;
    }


}

BoundingBoxAnswer.RequiredProperties = ["boxes"];

/**
 * @member {Array.<module:model/Corners>} boxes
 */
BoundingBoxAnswer.prototype['boxes'] = undefined;






export default BoundingBoxAnswer;
