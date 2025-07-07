external_url 'http://gitlab.home'

# Disable unnecessary services
nginx['enable'] = true
postgresql['enable'] = true
redis['enable'] = true
prometheus['enable'] = false
alertmanager['enable'] = false
node_exporter['enable'] = false
redis_exporter['enable'] = false
postgres_exporter['enable'] = false
gitlab_exporter['enable'] = false
mattermost['enable'] = false

# Resource limits
puma['worker_processes'] = 2
puma['min_threads'] = 2
puma['max_threads'] = 4
sidekiq['concurrency'] = 4

# Database settings
postgresql['shared_buffers'] = "256MB"
postgresql['max_worker_processes'] = 4
postgresql['max_parallel_workers_per_gather'] = 2

# Redis settings
redis['maxmemory'] = "256MB"
redis['maxmemory_policy'] = "allkeys-lru"

# Disable usage ping
gitlab_rails['usage_ping_enabled'] = false

# Disable auto migrations (for container environments)
gitlab_rails['auto_migrate'] = false
gitlab_rails['backup_keep_time'] = 604800  # 7 days
