# Infrastructure

The component pieces of the infrastructure are private VMs in azure.

The demo environment was bootstrapped with ansible and Splunkenizer. This resulted in a few [issues](https://github.com/splunkenizer/Splunkenizer/issues?q=is%3Aissue+author%3Amattuebel) but worked quite well overall.

The config that was fed into the primary deploying playbook:

```yaml
---
# splunk_config.yml
plugin: splunkenizer

general:
  url_locale: en-US

os:
  packages:
    - acl

custom:
  ansible_user: azureuser

splunk_defaults:
  splunk_license_file: Splunk_Enterprise.lic
  splunk_env_name: muebel_splunk
  splunk_version: latest
  splunk_download:
    splunk: true

  splunk_admin_password: changedit
  
  splunk_ssl:
    web:
      enable: true
      own_certs: false

splunk_idxclusters:
  - idxc_name: idxc1
    idxc_password: splunkidxc
    idxc_replication_port: 9887
    idxc_rf: 2
    idxc_sf: 2

splunk_shclusters:
  - shc_name: shc1
    shc_site: site0
    shc_password: splunkshc
    shc_replication_port: 9887

splunk_hosts:
  - name: cm.mattuebel.splunk.net
    roles:
      - cluster_master
      - license_master
    idxcluster: idxc1
    shcluster: shc1

  - list:
      - idx1.mattuebel.splunk.net
      - idx2.mattuebel.splunk.net
      - idx3.mattuebel.splunk.net
    roles:
      - indexer
    idxcluster: idxc1
  
  - list:
      - sh1.mattuebel.splunk.net
      - sh2.mattuebel.splunk.net
      - sh3.mattuebel.splunk.net
    roles:
      - search_head
    shcluster: shc1
  
  - name: shcdeployer.mattuebel.splunk.net
    roles:
      - deployer
    shcluster: shc1

  - name: ds.mattuebel.splunk.net
    roles:
      - deployment_server
  
  - name: hf.mattuebel.splunk.net
    roles:
      - heavy_forwarder
```

# Repos

The repos all have associated self-hosted runners installed on each of the controlling pieces (cm, ds, and shcdeployer).