{{- /*
secrets config
*/}}
{{- define "config.envs" -}}
- name: POLYAXON_K8S_NODE_NAME
  valueFrom:
    fieldRef:
      fieldPath: spec.nodeName
- name: POLYAXON_RABBITMQ_PASSWORD
  valueFrom:
    secretKeyRef:
{{- if (index .Values "rabbitmq-ha").enabled }}
      name: {{ template "rabbitmq.fullname" . }}
{{- else }}
      name: {{ template "polyaxon.fullname" . }}-rabbitmq-secret
{{- end }}
      key: rabbitmq-password
{{- if and .Values.redis.enabled .Values.redis.usePassword }}
- name: POLYAXON_REDIS_PASSWORD
  valueFrom:
    secretKeyRef:
      name: {{ template "redis.fullname" . }}
      key: redis-password
{{- end }}
{{- if and (not .Values.redis.enabled) .Values.externalServices.redis.usePassword }}
- name: POLYAXON_REDIS_PASSWORD
  valueFrom:
    secretKeyRef:
      name: {{ template "polyaxon.fullname" . }}-redis-secret
      key: redis-password
{{- end }}
- name: POLYAXON_DB_PASSWORD
  valueFrom:
    secretKeyRef:
{{- if .Values.postgresql.enabled }}
      name: {{ template "postgresql.fullname" . }}
{{- else }}
      name: {{ template "polyaxon.fullname" . }}-postgres-secret
{{- end }}
      key: postgres-password
{{- end -}}
