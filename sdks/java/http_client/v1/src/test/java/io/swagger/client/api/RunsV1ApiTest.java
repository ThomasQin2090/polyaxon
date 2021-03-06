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


package io.swagger.client.api;

import io.swagger.client.ApiException;
import java.io.File;
import io.swagger.client.model.V1ArtifactTreeResponse;
import io.swagger.client.model.V1Auth;
import io.swagger.client.model.V1CodeRef;
import io.swagger.client.model.V1EntityStatusBodyRequest;
import io.swagger.client.model.V1ListRunsResponse;
import io.swagger.client.model.V1ProjectEntityResourceRequest;
import io.swagger.client.model.V1Run;
import io.swagger.client.model.V1RunSettings;
import io.swagger.client.model.V1Status;
import io.swagger.client.model.V1Uuids;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for RunsV1Api
 */
@Ignore
public class RunsV1ApiTest {

    private final RunsV1Api api = new RunsV1Api();

    
    /**
     * Archive run
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void archiveRunTest() throws ApiException {
        String owner = null;
        String project = null;
        String uuid = null;
        api.archiveRun(owner, project, uuid);

        // TODO: test validations
    }
    
    /**
     * Bookmark run
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void bookmarkRunTest() throws ApiException {
        String owner = null;
        String project = null;
        String uuid = null;
        api.bookmarkRun(owner, project, uuid);

        // TODO: test validations
    }
    
    /**
     * Restart run with copy
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void copyRunTest() throws ApiException {
        String entityOwner = null;
        String entityProject = null;
        String entityUuid = null;
        V1Run body = null;
        V1Run response = api.copyRun(entityOwner, entityProject, entityUuid, body);

        // TODO: test validations
    }
    
    /**
     * Create new run
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void createRunTest() throws ApiException {
        String owner = null;
        String project = null;
        V1Run body = null;
        V1Run response = api.createRun(owner, project, body);

        // TODO: test validations
    }
    
    /**
     * Get run code ref
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void createRunCodeRefTest() throws ApiException {
        String entityOwner = null;
        String entityProject = null;
        String entityUuid = null;
        V1CodeRef body = null;
        api.createRunCodeRef(entityOwner, entityProject, entityUuid, body);

        // TODO: test validations
    }
    
    /**
     * Create new run status
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void createRunStatusTest() throws ApiException {
        String owner = null;
        String project = null;
        String uuid = null;
        V1EntityStatusBodyRequest body = null;
        V1Status response = api.createRunStatus(owner, project, uuid, body);

        // TODO: test validations
    }
    
    /**
     * Delete run
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void deleteRunTest() throws ApiException {
        String owner = null;
        String project = null;
        String uuid = null;
        api.deleteRun(owner, project, uuid);

        // TODO: test validations
    }
    
    /**
     * Delete runs
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void deleteRunsTest() throws ApiException {
        String owner = null;
        String project = null;
        V1Uuids body = null;
        api.deleteRuns(owner, project, body);

        // TODO: test validations
    }
    
    /**
     * Get run
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getRunTest() throws ApiException {
        String owner = null;
        String project = null;
        String uuid = null;
        V1Run response = api.getRun(owner, project, uuid);

        // TODO: test validations
    }
    
    /**
     * Get run artifacts list
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getRunArtifactsTreeTest() throws ApiException {
        String owner = null;
        String project = null;
        String uuid = null;
        String path = null;
        Integer step = null;
        String kind = null;
        V1ArtifactTreeResponse response = api.getRunArtifactsTree(owner, project, uuid, path, step, kind);

        // TODO: test validations
    }
    
    /**
     * Get run logs get file
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getRunLogsFileTest() throws ApiException {
        String owner = null;
        String project = null;
        String uuid = null;
        String path = null;
        Integer step = null;
        String type = null;
        String response = api.getRunLogsFile(owner, project, uuid, path, step, type);

        // TODO: test validations
    }
    
    /**
     * Get run logs list
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getRunLogsTreeTest() throws ApiException {
        String owner = null;
        String project = null;
        String uuid = null;
        String path = null;
        Integer step = null;
        String kind = null;
        V1ArtifactTreeResponse response = api.getRunLogsTree(owner, project, uuid, path, step, kind);

        // TODO: test validations
    }
    
    /**
     * Get Run settings
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getRunSettingsTest() throws ApiException {
        String owner = null;
        String project = null;
        String uuid = null;
        V1RunSettings response = api.getRunSettings(owner, project, uuid);

        // TODO: test validations
    }
    
    /**
     * Get run status
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getRunStatusesTest() throws ApiException {
        String owner = null;
        String project = null;
        String uuid = null;
        V1Status response = api.getRunStatuses(owner, project, uuid);

        // TODO: test validations
    }
    
    /**
     * Impersonate run token
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void impersonateTokenTest() throws ApiException {
        String owner = null;
        String project = null;
        String uuid = null;
        V1Auth response = api.impersonateToken(owner, project, uuid);

        // TODO: test validations
    }
    
    /**
     * Invalidate run
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void invalidateRunTest() throws ApiException {
        String owner = null;
        String project = null;
        String uuid = null;
        V1ProjectEntityResourceRequest body = null;
        api.invalidateRun(owner, project, uuid, body);

        // TODO: test validations
    }
    
    /**
     * Invalidate runs
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void invalidateRunsTest() throws ApiException {
        String owner = null;
        String project = null;
        V1Uuids body = null;
        api.invalidateRuns(owner, project, body);

        // TODO: test validations
    }
    
    /**
     * List archived runs for user
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void listArchivedRunsTest() throws ApiException {
        String user = null;
        Integer offset = null;
        Integer limit = null;
        String sort = null;
        String query = null;
        V1ListRunsResponse response = api.listArchivedRuns(user, offset, limit, sort, query);

        // TODO: test validations
    }
    
    /**
     * List bookmarked runs for user
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void listBookmarkedRunsTest() throws ApiException {
        String user = null;
        Integer offset = null;
        Integer limit = null;
        String sort = null;
        String query = null;
        V1ListRunsResponse response = api.listBookmarkedRuns(user, offset, limit, sort, query);

        // TODO: test validations
    }
    
    /**
     * List runs
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void listRunsTest() throws ApiException {
        String owner = null;
        String project = null;
        Integer offset = null;
        Integer limit = null;
        String sort = null;
        String query = null;
        V1ListRunsResponse response = api.listRuns(owner, project, offset, limit, sort, query);

        // TODO: test validations
    }
    
    /**
     * Patch run
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void patchRunTest() throws ApiException {
        String owner = null;
        String project = null;
        String runUuid = null;
        V1Run body = null;
        V1Run response = api.patchRun(owner, project, runUuid, body);

        // TODO: test validations
    }
    
    /**
     * Restart run
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void restartRunTest() throws ApiException {
        String entityOwner = null;
        String entityProject = null;
        String entityUuid = null;
        V1Run body = null;
        V1Run response = api.restartRun(entityOwner, entityProject, entityUuid, body);

        // TODO: test validations
    }
    
    /**
     * Restore run
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void restoreRunTest() throws ApiException {
        String owner = null;
        String project = null;
        String uuid = null;
        api.restoreRun(owner, project, uuid);

        // TODO: test validations
    }
    
    /**
     * Resume run
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void resumeRunTest() throws ApiException {
        String entityOwner = null;
        String entityProject = null;
        String entityUuid = null;
        V1Run body = null;
        V1Run response = api.resumeRun(entityOwner, entityProject, entityUuid, body);

        // TODO: test validations
    }
    
    /**
     * Start run tensorboard
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void startRunTensorboardTest() throws ApiException {
        String owner = null;
        String project = null;
        String uuid = null;
        V1ProjectEntityResourceRequest body = null;
        api.startRunTensorboard(owner, project, uuid, body);

        // TODO: test validations
    }
    
    /**
     * Stop run
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void stopRunTest() throws ApiException {
        String owner = null;
        String project = null;
        String uuid = null;
        api.stopRun(owner, project, uuid);

        // TODO: test validations
    }
    
    /**
     * Stop run tensorboard
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void stopRunTensorboardTest() throws ApiException {
        String owner = null;
        String project = null;
        String uuid = null;
        api.stopRunTensorboard(owner, project, uuid);

        // TODO: test validations
    }
    
    /**
     * Stop runs
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void stopRunsTest() throws ApiException {
        String owner = null;
        String project = null;
        V1Uuids body = null;
        api.stopRuns(owner, project, body);

        // TODO: test validations
    }
    
    /**
     * Unbookmark run
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void unbookmarkRunTest() throws ApiException {
        String owner = null;
        String project = null;
        String uuid = null;
        api.unbookmarkRun(owner, project, uuid);

        // TODO: test validations
    }
    
    /**
     * Update run
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void updateRunTest() throws ApiException {
        String owner = null;
        String project = null;
        String runUuid = null;
        V1Run body = null;
        V1Run response = api.updateRun(owner, project, runUuid, body);

        // TODO: test validations
    }
    
    /**
     * Upload an artifact file to a store via run access
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void uploadRunArtifactTest() throws ApiException {
        String owner = null;
        String project = null;
        String uuid = null;
        File uploadfile = null;
        String path = null;
        Boolean overwrite = null;
        api.uploadRunArtifact(owner, project, uuid, uploadfile, path, overwrite);

        // TODO: test validations
    }
    
    /**
     * Upload a logs file to a store via run access
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void uploadRunLogsTest() throws ApiException {
        String owner = null;
        String project = null;
        String uuid = null;
        File uploadfile = null;
        String path = null;
        Boolean overwrite = null;
        api.uploadRunLogs(owner, project, uuid, uploadfile, path, overwrite);

        // TODO: test validations
    }
    
}
