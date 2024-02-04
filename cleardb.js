const sdk = require('api')('@astra/v2.0#1mld74kq6wdonq');

sdk.getApiRestV2NamespacesNamespaceIdCollectionsCollectionId({
  where: '',
  sort: '',
  'namespace-id': 'namespace-id',
  'collection-id': 'collection-id'
})
  .then(({ data }) => console.log(data))
  .catch(err => console.error(err));