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
 * Do not edit the class manually.
 */


package io.swagger.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * V1IO
 */

public class V1IO {
  @SerializedName("name")
  private String name = null;

  @SerializedName("description")
  private String description = null;

  @SerializedName("iotype")
  private String iotype = null;

  @SerializedName("value")
  private Object value = null;

  @SerializedName("is_optional")
  private Boolean isOptional = null;

  @SerializedName("is_list")
  private Boolean isList = null;

  @SerializedName("is_flag")
  private Boolean isFlag = null;

  @SerializedName("options")
  private List<Object> options = null;

  public V1IO name(String name) {
    this.name = name;
    return this;
  }

   /**
   * Get name
   * @return name
  **/
  @ApiModelProperty(value = "")
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public V1IO description(String description) {
    this.description = description;
    return this;
  }

   /**
   * Get description
   * @return description
  **/
  @ApiModelProperty(value = "")
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }

  public V1IO iotype(String iotype) {
    this.iotype = iotype;
    return this;
  }

   /**
   * Get iotype
   * @return iotype
  **/
  @ApiModelProperty(value = "")
  public String getIotype() {
    return iotype;
  }

  public void setIotype(String iotype) {
    this.iotype = iotype;
  }

  public V1IO value(Object value) {
    this.value = value;
    return this;
  }

   /**
   * Get value
   * @return value
  **/
  @ApiModelProperty(value = "")
  public Object getValue() {
    return value;
  }

  public void setValue(Object value) {
    this.value = value;
  }

  public V1IO isOptional(Boolean isOptional) {
    this.isOptional = isOptional;
    return this;
  }

   /**
   * Get isOptional
   * @return isOptional
  **/
  @ApiModelProperty(value = "")
  public Boolean isIsOptional() {
    return isOptional;
  }

  public void setIsOptional(Boolean isOptional) {
    this.isOptional = isOptional;
  }

  public V1IO isList(Boolean isList) {
    this.isList = isList;
    return this;
  }

   /**
   * Get isList
   * @return isList
  **/
  @ApiModelProperty(value = "")
  public Boolean isIsList() {
    return isList;
  }

  public void setIsList(Boolean isList) {
    this.isList = isList;
  }

  public V1IO isFlag(Boolean isFlag) {
    this.isFlag = isFlag;
    return this;
  }

   /**
   * Get isFlag
   * @return isFlag
  **/
  @ApiModelProperty(value = "")
  public Boolean isIsFlag() {
    return isFlag;
  }

  public void setIsFlag(Boolean isFlag) {
    this.isFlag = isFlag;
  }

  public V1IO options(List<Object> options) {
    this.options = options;
    return this;
  }

  public V1IO addOptionsItem(Object optionsItem) {
    if (this.options == null) {
      this.options = new ArrayList<Object>();
    }
    this.options.add(optionsItem);
    return this;
  }

   /**
   * Get options
   * @return options
  **/
  @ApiModelProperty(value = "")
  public List<Object> getOptions() {
    return options;
  }

  public void setOptions(List<Object> options) {
    this.options = options;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    V1IO v1IO = (V1IO) o;
    return Objects.equals(this.name, v1IO.name) &&
        Objects.equals(this.description, v1IO.description) &&
        Objects.equals(this.iotype, v1IO.iotype) &&
        Objects.equals(this.value, v1IO.value) &&
        Objects.equals(this.isOptional, v1IO.isOptional) &&
        Objects.equals(this.isList, v1IO.isList) &&
        Objects.equals(this.isFlag, v1IO.isFlag) &&
        Objects.equals(this.options, v1IO.options);
  }

  @Override
  public int hashCode() {
    return Objects.hash(name, description, iotype, value, isOptional, isList, isFlag, options);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class V1IO {\n");
    
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    iotype: ").append(toIndentedString(iotype)).append("\n");
    sb.append("    value: ").append(toIndentedString(value)).append("\n");
    sb.append("    isOptional: ").append(toIndentedString(isOptional)).append("\n");
    sb.append("    isList: ").append(toIndentedString(isList)).append("\n");
    sb.append("    isFlag: ").append(toIndentedString(isFlag)).append("\n");
    sb.append("    options: ").append(toIndentedString(options)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

