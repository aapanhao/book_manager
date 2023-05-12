# gen python protos code path
target_p='book_manager'
# project proto path
source_p='protos'
# service
service_list=("book" "user")

rm -r "${target_p:?}/${source_p:?}"*
mkdir -p "${target_p:?}/${source_p:?}"

for service in "${service_list[@]}"
do
  mkdir -p "${target_p:?}/${source_p:?}/${service:?}"
  echo  "from proto file:" $source_p/"$service"/*.proto "gen proto py file to" $target_p/$source_p
  ${VENV_PREFIX}python -m grpc_tools.protoc \
    --mypy_grpc_out=./$target_p \
    --mypy_out=./$target_p \
    --python_out=./$target_p \
    --grpc_python_out=./$target_p \
    -I. \
    $source_p/"$service"/*.proto

  touch $target_p/$source_p/"$service"/__init__.py
  # fix grpc tools bug
  sed -i '' "s/from protos.$service import/from . import/" $target_p/$source_p/$service/*.py
done