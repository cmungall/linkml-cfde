# Auto generated from linkml_cfde.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-07-08T12:46:39
# Schema: test-schema
#
# id: http://example.org/test/
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Datetime, Decimal, Integer, String
from linkml_runtime.utils.metamodelcore import Bool, Decimal, XSDDateTime

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CFDE_DISEASE_ASSOCIATION_TYPE = CurieNamespace('cfde_disease_association_type', 'http://example.org/test//cfde_disease_association_type/')
CFDE_PHENOTYPE_ASSOCIATION_TYPE = CurieNamespace('cfde_phenotype_association_type', 'http://example.org/test//cfde_phenotype_association_type/')
CFDE_SUBJECT_ETHNICITY = CurieNamespace('cfde_subject_ethnicity', 'http://example.org/test//cfde_subject_ethnicity/')
CFDE_SUBJECT_GRANULARITY = CurieNamespace('cfde_subject_granularity', 'http://example.org/test//cfde_subject_granularity/')
CFDE_SUBJECT_RACE = CurieNamespace('cfde_subject_race', 'http://example.org/test//cfde_subject_race/')
CFDE_SUBJECT_ROLE = CurieNamespace('cfde_subject_role', 'http://example.org/test//cfde_subject_role/')
CFDE_SUBJECT_SEX = CurieNamespace('cfde_subject_sex', 'http://example.org/test//cfde_subject_sex/')
EX = CurieNamespace('ex', 'https://example.org/test/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = EX


# Types

# Class references



@dataclass
class File(YAMLRoot):
    """
    ['A stable digital asset']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.File
    class_class_curie: ClassVar[str] = "ex:File"
    class_name: ClassVar[str] = "file"
    class_model_uri: ClassVar[URIRef] = EX.File

    id_namespace: str = None
    local_id: str = None
    project_id_namespace: str = None
    project_local_id: str = None
    persistent_id: Optional[str] = None
    creation_time: Optional[Union[str, XSDDateTime]] = None
    size_in_bytes: Optional[int] = None
    uncompressed_size_in_bytes: Optional[int] = None
    sha256: Optional[str] = None
    md5: Optional[str] = None
    filename: Optional[str] = None
    file_format: Optional[str] = None
    compression_format: Optional[str] = None
    data_type: Optional[str] = None
    assay_type: Optional[str] = None
    analysis_type: Optional[str] = None
    mime_type: Optional[str] = None
    bundle_collection_id_namespace: Optional[str] = None
    bundle_collection_local_id: Optional[str] = None
    dbgap_study_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id_namespace):
            self.MissingRequiredField("id_namespace")
        if not isinstance(self.id_namespace, str):
            self.id_namespace = str(self.id_namespace)

        if self._is_empty(self.local_id):
            self.MissingRequiredField("local_id")
        if not isinstance(self.local_id, str):
            self.local_id = str(self.local_id)

        if self._is_empty(self.project_id_namespace):
            self.MissingRequiredField("project_id_namespace")
        if not isinstance(self.project_id_namespace, str):
            self.project_id_namespace = str(self.project_id_namespace)

        if self._is_empty(self.project_local_id):
            self.MissingRequiredField("project_local_id")
        if not isinstance(self.project_local_id, str):
            self.project_local_id = str(self.project_local_id)

        if self.persistent_id is not None and not isinstance(self.persistent_id, str):
            self.persistent_id = str(self.persistent_id)

        if self.creation_time is not None and not isinstance(self.creation_time, XSDDateTime):
            self.creation_time = XSDDateTime(self.creation_time)

        if self.size_in_bytes is not None and not isinstance(self.size_in_bytes, int):
            self.size_in_bytes = int(self.size_in_bytes)

        if self.uncompressed_size_in_bytes is not None and not isinstance(self.uncompressed_size_in_bytes, int):
            self.uncompressed_size_in_bytes = int(self.uncompressed_size_in_bytes)

        if self.sha256 is not None and not isinstance(self.sha256, str):
            self.sha256 = str(self.sha256)

        if self.md5 is not None and not isinstance(self.md5, str):
            self.md5 = str(self.md5)

        if self.filename is not None and not isinstance(self.filename, str):
            self.filename = str(self.filename)

        if self.file_format is not None and not isinstance(self.file_format, str):
            self.file_format = str(self.file_format)

        if self.compression_format is not None and not isinstance(self.compression_format, str):
            self.compression_format = str(self.compression_format)

        if self.data_type is not None and not isinstance(self.data_type, str):
            self.data_type = str(self.data_type)

        if self.assay_type is not None and not isinstance(self.assay_type, str):
            self.assay_type = str(self.assay_type)

        if self.analysis_type is not None and not isinstance(self.analysis_type, str):
            self.analysis_type = str(self.analysis_type)

        if self.mime_type is not None and not isinstance(self.mime_type, str):
            self.mime_type = str(self.mime_type)

        if self.bundle_collection_id_namespace is not None and not isinstance(self.bundle_collection_id_namespace, str):
            self.bundle_collection_id_namespace = str(self.bundle_collection_id_namespace)

        if self.bundle_collection_local_id is not None and not isinstance(self.bundle_collection_local_id, str):
            self.bundle_collection_local_id = str(self.bundle_collection_local_id)

        if self.dbgap_study_id is not None and not isinstance(self.dbgap_study_id, str):
            self.dbgap_study_id = str(self.dbgap_study_id)

        super().__post_init__(**kwargs)


@dataclass
class Biosample(YAMLRoot):
    """
    ['A tissue sample or other physical specimen']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.Biosample
    class_class_curie: ClassVar[str] = "ex:Biosample"
    class_name: ClassVar[str] = "biosample"
    class_model_uri: ClassVar[URIRef] = EX.Biosample

    id_namespace: str = None
    local_id: str = None
    project_id_namespace: str = None
    project_local_id: str = None
    persistent_id: Optional[str] = None
    creation_time: Optional[Union[str, XSDDateTime]] = None
    assay_type: Optional[str] = None
    anatomy: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id_namespace):
            self.MissingRequiredField("id_namespace")
        if not isinstance(self.id_namespace, str):
            self.id_namespace = str(self.id_namespace)

        if self._is_empty(self.local_id):
            self.MissingRequiredField("local_id")
        if not isinstance(self.local_id, str):
            self.local_id = str(self.local_id)

        if self._is_empty(self.project_id_namespace):
            self.MissingRequiredField("project_id_namespace")
        if not isinstance(self.project_id_namespace, str):
            self.project_id_namespace = str(self.project_id_namespace)

        if self._is_empty(self.project_local_id):
            self.MissingRequiredField("project_local_id")
        if not isinstance(self.project_local_id, str):
            self.project_local_id = str(self.project_local_id)

        if self.persistent_id is not None and not isinstance(self.persistent_id, str):
            self.persistent_id = str(self.persistent_id)

        if self.creation_time is not None and not isinstance(self.creation_time, XSDDateTime):
            self.creation_time = XSDDateTime(self.creation_time)

        if self.assay_type is not None and not isinstance(self.assay_type, str):
            self.assay_type = str(self.assay_type)

        if self.anatomy is not None and not isinstance(self.anatomy, str):
            self.anatomy = str(self.anatomy)

        super().__post_init__(**kwargs)


@dataclass
class Subject(YAMLRoot):
    """
    ['A biological entity from which a C2M2 biosample can in principle be generated']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.Subject
    class_class_curie: ClassVar[str] = "ex:Subject"
    class_name: ClassVar[str] = "subject"
    class_model_uri: ClassVar[URIRef] = EX.Subject

    id_namespace: str = None
    local_id: str = None
    project_id_namespace: str = None
    project_local_id: str = None
    granularity: Union[str, "GranularityEnum"] = None
    persistent_id: Optional[str] = None
    creation_time: Optional[Union[str, XSDDateTime]] = None
    sex: Optional[Union[str, "SexEnum"]] = None
    ethnicity: Optional[Union[str, "EthnicityEnum"]] = None
    age_at_enrollment: Optional[Decimal] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id_namespace):
            self.MissingRequiredField("id_namespace")
        if not isinstance(self.id_namespace, str):
            self.id_namespace = str(self.id_namespace)

        if self._is_empty(self.local_id):
            self.MissingRequiredField("local_id")
        if not isinstance(self.local_id, str):
            self.local_id = str(self.local_id)

        if self._is_empty(self.project_id_namespace):
            self.MissingRequiredField("project_id_namespace")
        if not isinstance(self.project_id_namespace, str):
            self.project_id_namespace = str(self.project_id_namespace)

        if self._is_empty(self.project_local_id):
            self.MissingRequiredField("project_local_id")
        if not isinstance(self.project_local_id, str):
            self.project_local_id = str(self.project_local_id)

        if self._is_empty(self.granularity):
            self.MissingRequiredField("granularity")
        if not isinstance(self.granularity, GranularityEnum):
            self.granularity = GranularityEnum(self.granularity)

        if self.persistent_id is not None and not isinstance(self.persistent_id, str):
            self.persistent_id = str(self.persistent_id)

        if self.creation_time is not None and not isinstance(self.creation_time, XSDDateTime):
            self.creation_time = XSDDateTime(self.creation_time)

        if self.sex is not None and not isinstance(self.sex, SexEnum):
            self.sex = SexEnum(self.sex)

        if self.ethnicity is not None and not isinstance(self.ethnicity, EthnicityEnum):
            self.ethnicity = EthnicityEnum(self.ethnicity)

        if self.age_at_enrollment is not None and not isinstance(self.age_at_enrollment, Decimal):
            self.age_at_enrollment = Decimal(self.age_at_enrollment)

        super().__post_init__(**kwargs)


@dataclass
class Dcc(YAMLRoot):
    """
    ['The Common Fund program or data coordinating center (DCC, identified by the given project foreign key) that
    produced this C2M2 instance']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.Dcc
    class_class_curie: ClassVar[str] = "ex:Dcc"
    class_name: ClassVar[str] = "dcc"
    class_model_uri: ClassVar[URIRef] = EX.Dcc

    id: str = None
    dcc_name: str = None
    dcc_abbreviation: str = None
    contact_email: str = None
    contact_name: str = None
    dcc_url: str = None
    project_id_namespace: str = None
    project_local_id: str = None
    dcc_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.dcc_name):
            self.MissingRequiredField("dcc_name")
        if not isinstance(self.dcc_name, str):
            self.dcc_name = str(self.dcc_name)

        if self._is_empty(self.dcc_abbreviation):
            self.MissingRequiredField("dcc_abbreviation")
        if not isinstance(self.dcc_abbreviation, str):
            self.dcc_abbreviation = str(self.dcc_abbreviation)

        if self._is_empty(self.contact_email):
            self.MissingRequiredField("contact_email")
        if not isinstance(self.contact_email, str):
            self.contact_email = str(self.contact_email)

        if self._is_empty(self.contact_name):
            self.MissingRequiredField("contact_name")
        if not isinstance(self.contact_name, str):
            self.contact_name = str(self.contact_name)

        if self._is_empty(self.dcc_url):
            self.MissingRequiredField("dcc_url")
        if not isinstance(self.dcc_url, str):
            self.dcc_url = str(self.dcc_url)

        if self._is_empty(self.project_id_namespace):
            self.MissingRequiredField("project_id_namespace")
        if not isinstance(self.project_id_namespace, str):
            self.project_id_namespace = str(self.project_id_namespace)

        if self._is_empty(self.project_local_id):
            self.MissingRequiredField("project_local_id")
        if not isinstance(self.project_local_id, str):
            self.project_local_id = str(self.project_local_id)

        if self.dcc_description is not None and not isinstance(self.dcc_description, str):
            self.dcc_description = str(self.dcc_description)

        super().__post_init__(**kwargs)


@dataclass
class Project(YAMLRoot):
    """
    ["A node in the C2M2 project hierarchy subdividing all resources described by this DCC's C2M2 metadata"]
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.Project
    class_class_curie: ClassVar[str] = "ex:Project"
    class_name: ClassVar[str] = "project"
    class_model_uri: ClassVar[URIRef] = EX.Project

    id_namespace: str = None
    local_id: str = None
    persistent_id: Optional[str] = None
    creation_time: Optional[Union[str, XSDDateTime]] = None
    abbreviation: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id_namespace):
            self.MissingRequiredField("id_namespace")
        if not isinstance(self.id_namespace, str):
            self.id_namespace = str(self.id_namespace)

        if self._is_empty(self.local_id):
            self.MissingRequiredField("local_id")
        if not isinstance(self.local_id, str):
            self.local_id = str(self.local_id)

        if self.persistent_id is not None and not isinstance(self.persistent_id, str):
            self.persistent_id = str(self.persistent_id)

        if self.creation_time is not None and not isinstance(self.creation_time, XSDDateTime):
            self.creation_time = XSDDateTime(self.creation_time)

        if self.abbreviation is not None and not isinstance(self.abbreviation, str):
            self.abbreviation = str(self.abbreviation)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class ProjectInProject(YAMLRoot):
    """
    ['Association between a child project and its parent']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.ProjectInProject
    class_class_curie: ClassVar[str] = "ex:ProjectInProject"
    class_name: ClassVar[str] = "project_in_project"
    class_model_uri: ClassVar[URIRef] = EX.ProjectInProject

    parent_project_id_namespace: str = None
    parent_project_local_id: str = None
    child_project_id_namespace: str = None
    child_project_local_id: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.parent_project_id_namespace):
            self.MissingRequiredField("parent_project_id_namespace")
        if not isinstance(self.parent_project_id_namespace, str):
            self.parent_project_id_namespace = str(self.parent_project_id_namespace)

        if self._is_empty(self.parent_project_local_id):
            self.MissingRequiredField("parent_project_local_id")
        if not isinstance(self.parent_project_local_id, str):
            self.parent_project_local_id = str(self.parent_project_local_id)

        if self._is_empty(self.child_project_id_namespace):
            self.MissingRequiredField("child_project_id_namespace")
        if not isinstance(self.child_project_id_namespace, str):
            self.child_project_id_namespace = str(self.child_project_id_namespace)

        if self._is_empty(self.child_project_local_id):
            self.MissingRequiredField("child_project_local_id")
        if not isinstance(self.child_project_local_id, str):
            self.child_project_local_id = str(self.child_project_local_id)

        super().__post_init__(**kwargs)


@dataclass
class Collection(YAMLRoot):
    """
    ['A grouping of C2M2 files, biosamples and/or subjects']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.Collection
    class_class_curie: ClassVar[str] = "ex:Collection"
    class_name: ClassVar[str] = "collection"
    class_model_uri: ClassVar[URIRef] = EX.Collection

    id_namespace: str = None
    local_id: str = None
    persistent_id: Optional[str] = None
    creation_time: Optional[Union[str, XSDDateTime]] = None
    abbreviation: Optional[str] = None
    description: Optional[str] = None
    has_time_series_data: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id_namespace):
            self.MissingRequiredField("id_namespace")
        if not isinstance(self.id_namespace, str):
            self.id_namespace = str(self.id_namespace)

        if self._is_empty(self.local_id):
            self.MissingRequiredField("local_id")
        if not isinstance(self.local_id, str):
            self.local_id = str(self.local_id)

        if self.persistent_id is not None and not isinstance(self.persistent_id, str):
            self.persistent_id = str(self.persistent_id)

        if self.creation_time is not None and not isinstance(self.creation_time, XSDDateTime):
            self.creation_time = XSDDateTime(self.creation_time)

        if self.abbreviation is not None and not isinstance(self.abbreviation, str):
            self.abbreviation = str(self.abbreviation)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.has_time_series_data is not None and not isinstance(self.has_time_series_data, Bool):
            self.has_time_series_data = Bool(self.has_time_series_data)

        super().__post_init__(**kwargs)


@dataclass
class CollectionInCollection(YAMLRoot):
    """
    ['Association between a containing collection (superset) and a contained collection (subset)']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.CollectionInCollection
    class_class_curie: ClassVar[str] = "ex:CollectionInCollection"
    class_name: ClassVar[str] = "collection_in_collection"
    class_model_uri: ClassVar[URIRef] = EX.CollectionInCollection

    superset_collection_id_namespace: str = None
    superset_collection_local_id: str = None
    subset_collection_id_namespace: str = None
    subset_collection_local_id: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.superset_collection_id_namespace):
            self.MissingRequiredField("superset_collection_id_namespace")
        if not isinstance(self.superset_collection_id_namespace, str):
            self.superset_collection_id_namespace = str(self.superset_collection_id_namespace)

        if self._is_empty(self.superset_collection_local_id):
            self.MissingRequiredField("superset_collection_local_id")
        if not isinstance(self.superset_collection_local_id, str):
            self.superset_collection_local_id = str(self.superset_collection_local_id)

        if self._is_empty(self.subset_collection_id_namespace):
            self.MissingRequiredField("subset_collection_id_namespace")
        if not isinstance(self.subset_collection_id_namespace, str):
            self.subset_collection_id_namespace = str(self.subset_collection_id_namespace)

        if self._is_empty(self.subset_collection_local_id):
            self.MissingRequiredField("subset_collection_local_id")
        if not isinstance(self.subset_collection_local_id, str):
            self.subset_collection_local_id = str(self.subset_collection_local_id)

        super().__post_init__(**kwargs)


@dataclass
class FileDescribesCollection(YAMLRoot):
    """
    ['Association between a summary file and an entire collection described by that file']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.FileDescribesCollection
    class_class_curie: ClassVar[str] = "ex:FileDescribesCollection"
    class_name: ClassVar[str] = "file_describes_collection"
    class_model_uri: ClassVar[URIRef] = EX.FileDescribesCollection

    file_id_namespace: str = None
    file_local_id: str = None
    collection_id_namespace: str = None
    collection_local_id: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.file_id_namespace):
            self.MissingRequiredField("file_id_namespace")
        if not isinstance(self.file_id_namespace, str):
            self.file_id_namespace = str(self.file_id_namespace)

        if self._is_empty(self.file_local_id):
            self.MissingRequiredField("file_local_id")
        if not isinstance(self.file_local_id, str):
            self.file_local_id = str(self.file_local_id)

        if self._is_empty(self.collection_id_namespace):
            self.MissingRequiredField("collection_id_namespace")
        if not isinstance(self.collection_id_namespace, str):
            self.collection_id_namespace = str(self.collection_id_namespace)

        if self._is_empty(self.collection_local_id):
            self.MissingRequiredField("collection_local_id")
        if not isinstance(self.collection_local_id, str):
            self.collection_local_id = str(self.collection_local_id)

        super().__post_init__(**kwargs)


@dataclass
class CollectionDefinedByProject(YAMLRoot):
    """
    ['(Shallow) association between a collection and a project that defined it']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.CollectionDefinedByProject
    class_class_curie: ClassVar[str] = "ex:CollectionDefinedByProject"
    class_name: ClassVar[str] = "collection_defined_by_project"
    class_model_uri: ClassVar[URIRef] = EX.CollectionDefinedByProject

    collection_id_namespace: str = None
    collection_local_id: str = None
    project_id_namespace: str = None
    project_local_id: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.collection_id_namespace):
            self.MissingRequiredField("collection_id_namespace")
        if not isinstance(self.collection_id_namespace, str):
            self.collection_id_namespace = str(self.collection_id_namespace)

        if self._is_empty(self.collection_local_id):
            self.MissingRequiredField("collection_local_id")
        if not isinstance(self.collection_local_id, str):
            self.collection_local_id = str(self.collection_local_id)

        if self._is_empty(self.project_id_namespace):
            self.MissingRequiredField("project_id_namespace")
        if not isinstance(self.project_id_namespace, str):
            self.project_id_namespace = str(self.project_id_namespace)

        if self._is_empty(self.project_local_id):
            self.MissingRequiredField("project_local_id")
        if not isinstance(self.project_local_id, str):
            self.project_local_id = str(self.project_local_id)

        super().__post_init__(**kwargs)


@dataclass
class FileInCollection(YAMLRoot):
    """
    ['Association between a file and a (containing) collection']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.FileInCollection
    class_class_curie: ClassVar[str] = "ex:FileInCollection"
    class_name: ClassVar[str] = "file_in_collection"
    class_model_uri: ClassVar[URIRef] = EX.FileInCollection

    file_id_namespace: str = None
    file_local_id: str = None
    collection_id_namespace: str = None
    collection_local_id: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.file_id_namespace):
            self.MissingRequiredField("file_id_namespace")
        if not isinstance(self.file_id_namespace, str):
            self.file_id_namespace = str(self.file_id_namespace)

        if self._is_empty(self.file_local_id):
            self.MissingRequiredField("file_local_id")
        if not isinstance(self.file_local_id, str):
            self.file_local_id = str(self.file_local_id)

        if self._is_empty(self.collection_id_namespace):
            self.MissingRequiredField("collection_id_namespace")
        if not isinstance(self.collection_id_namespace, str):
            self.collection_id_namespace = str(self.collection_id_namespace)

        if self._is_empty(self.collection_local_id):
            self.MissingRequiredField("collection_local_id")
        if not isinstance(self.collection_local_id, str):
            self.collection_local_id = str(self.collection_local_id)

        super().__post_init__(**kwargs)


@dataclass
class BiosampleInCollection(YAMLRoot):
    """
    ['Association between a biosample and a (containing) collection']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.BiosampleInCollection
    class_class_curie: ClassVar[str] = "ex:BiosampleInCollection"
    class_name: ClassVar[str] = "biosample_in_collection"
    class_model_uri: ClassVar[URIRef] = EX.BiosampleInCollection

    biosample_id_namespace: str = None
    biosample_local_id: str = None
    collection_id_namespace: str = None
    collection_local_id: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.biosample_id_namespace):
            self.MissingRequiredField("biosample_id_namespace")
        if not isinstance(self.biosample_id_namespace, str):
            self.biosample_id_namespace = str(self.biosample_id_namespace)

        if self._is_empty(self.biosample_local_id):
            self.MissingRequiredField("biosample_local_id")
        if not isinstance(self.biosample_local_id, str):
            self.biosample_local_id = str(self.biosample_local_id)

        if self._is_empty(self.collection_id_namespace):
            self.MissingRequiredField("collection_id_namespace")
        if not isinstance(self.collection_id_namespace, str):
            self.collection_id_namespace = str(self.collection_id_namespace)

        if self._is_empty(self.collection_local_id):
            self.MissingRequiredField("collection_local_id")
        if not isinstance(self.collection_local_id, str):
            self.collection_local_id = str(self.collection_local_id)

        super().__post_init__(**kwargs)


@dataclass
class SubjectInCollection(YAMLRoot):
    """
    ['Association between a subject and a (containing) collection']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.SubjectInCollection
    class_class_curie: ClassVar[str] = "ex:SubjectInCollection"
    class_name: ClassVar[str] = "subject_in_collection"
    class_model_uri: ClassVar[URIRef] = EX.SubjectInCollection

    subject_id_namespace: str = None
    subject_local_id: str = None
    collection_id_namespace: str = None
    collection_local_id: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject_id_namespace):
            self.MissingRequiredField("subject_id_namespace")
        if not isinstance(self.subject_id_namespace, str):
            self.subject_id_namespace = str(self.subject_id_namespace)

        if self._is_empty(self.subject_local_id):
            self.MissingRequiredField("subject_local_id")
        if not isinstance(self.subject_local_id, str):
            self.subject_local_id = str(self.subject_local_id)

        if self._is_empty(self.collection_id_namespace):
            self.MissingRequiredField("collection_id_namespace")
        if not isinstance(self.collection_id_namespace, str):
            self.collection_id_namespace = str(self.collection_id_namespace)

        if self._is_empty(self.collection_local_id):
            self.MissingRequiredField("collection_local_id")
        if not isinstance(self.collection_local_id, str):
            self.collection_local_id = str(self.collection_local_id)

        super().__post_init__(**kwargs)


@dataclass
class FileDescribesBiosample(YAMLRoot):
    """
    ['Association between a biosample and a file containing information about that biosample']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.FileDescribesBiosample
    class_class_curie: ClassVar[str] = "ex:FileDescribesBiosample"
    class_name: ClassVar[str] = "file_describes_biosample"
    class_model_uri: ClassVar[URIRef] = EX.FileDescribesBiosample

    file_id_namespace: str = None
    file_local_id: str = None
    biosample_id_namespace: str = None
    biosample_local_id: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.file_id_namespace):
            self.MissingRequiredField("file_id_namespace")
        if not isinstance(self.file_id_namespace, str):
            self.file_id_namespace = str(self.file_id_namespace)

        if self._is_empty(self.file_local_id):
            self.MissingRequiredField("file_local_id")
        if not isinstance(self.file_local_id, str):
            self.file_local_id = str(self.file_local_id)

        if self._is_empty(self.biosample_id_namespace):
            self.MissingRequiredField("biosample_id_namespace")
        if not isinstance(self.biosample_id_namespace, str):
            self.biosample_id_namespace = str(self.biosample_id_namespace)

        if self._is_empty(self.biosample_local_id):
            self.MissingRequiredField("biosample_local_id")
        if not isinstance(self.biosample_local_id, str):
            self.biosample_local_id = str(self.biosample_local_id)

        super().__post_init__(**kwargs)


@dataclass
class FileDescribesSubject(YAMLRoot):
    """
    ['Association between a subject and a file containing information about that subject']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.FileDescribesSubject
    class_class_curie: ClassVar[str] = "ex:FileDescribesSubject"
    class_name: ClassVar[str] = "file_describes_subject"
    class_model_uri: ClassVar[URIRef] = EX.FileDescribesSubject

    file_id_namespace: str = None
    file_local_id: str = None
    subject_id_namespace: str = None
    subject_local_id: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.file_id_namespace):
            self.MissingRequiredField("file_id_namespace")
        if not isinstance(self.file_id_namespace, str):
            self.file_id_namespace = str(self.file_id_namespace)

        if self._is_empty(self.file_local_id):
            self.MissingRequiredField("file_local_id")
        if not isinstance(self.file_local_id, str):
            self.file_local_id = str(self.file_local_id)

        if self._is_empty(self.subject_id_namespace):
            self.MissingRequiredField("subject_id_namespace")
        if not isinstance(self.subject_id_namespace, str):
            self.subject_id_namespace = str(self.subject_id_namespace)

        if self._is_empty(self.subject_local_id):
            self.MissingRequiredField("subject_local_id")
        if not isinstance(self.subject_local_id, str):
            self.subject_local_id = str(self.subject_local_id)

        super().__post_init__(**kwargs)


@dataclass
class BiosampleFromSubject(YAMLRoot):
    """
    ['Association between a biosample and its source subject']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.BiosampleFromSubject
    class_class_curie: ClassVar[str] = "ex:BiosampleFromSubject"
    class_name: ClassVar[str] = "biosample_from_subject"
    class_model_uri: ClassVar[URIRef] = EX.BiosampleFromSubject

    biosample_id_namespace: str = None
    biosample_local_id: str = None
    subject_id_namespace: str = None
    subject_local_id: str = None
    age_at_sampling: Optional[Decimal] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.biosample_id_namespace):
            self.MissingRequiredField("biosample_id_namespace")
        if not isinstance(self.biosample_id_namespace, str):
            self.biosample_id_namespace = str(self.biosample_id_namespace)

        if self._is_empty(self.biosample_local_id):
            self.MissingRequiredField("biosample_local_id")
        if not isinstance(self.biosample_local_id, str):
            self.biosample_local_id = str(self.biosample_local_id)

        if self._is_empty(self.subject_id_namespace):
            self.MissingRequiredField("subject_id_namespace")
        if not isinstance(self.subject_id_namespace, str):
            self.subject_id_namespace = str(self.subject_id_namespace)

        if self._is_empty(self.subject_local_id):
            self.MissingRequiredField("subject_local_id")
        if not isinstance(self.subject_local_id, str):
            self.subject_local_id = str(self.subject_local_id)

        if self.age_at_sampling is not None and not isinstance(self.age_at_sampling, Decimal):
            self.age_at_sampling = Decimal(self.age_at_sampling)

        super().__post_init__(**kwargs)


@dataclass
class BiosampleDisease(YAMLRoot):
    """
    ['Association between a C2M2 biosample and a disease positively (e.g. cancer tumor tissue sample) OR negatively
    (e.g. cancer-free tissue sample) identified for that biosample']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.BiosampleDisease
    class_class_curie: ClassVar[str] = "ex:BiosampleDisease"
    class_name: ClassVar[str] = "biosample_disease"
    class_model_uri: ClassVar[URIRef] = EX.BiosampleDisease

    biosample_id_namespace: str = None
    biosample_local_id: str = None
    association_type: Union[str, "AssociationTypeEnum"] = None
    disease: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.biosample_id_namespace):
            self.MissingRequiredField("biosample_id_namespace")
        if not isinstance(self.biosample_id_namespace, str):
            self.biosample_id_namespace = str(self.biosample_id_namespace)

        if self._is_empty(self.biosample_local_id):
            self.MissingRequiredField("biosample_local_id")
        if not isinstance(self.biosample_local_id, str):
            self.biosample_local_id = str(self.biosample_local_id)

        if self._is_empty(self.association_type):
            self.MissingRequiredField("association_type")
        if not isinstance(self.association_type, AssociationTypeEnum):
            self.association_type = AssociationTypeEnum(self.association_type)

        if self._is_empty(self.disease):
            self.MissingRequiredField("disease")
        if not isinstance(self.disease, str):
            self.disease = str(self.disease)

        super().__post_init__(**kwargs)


@dataclass
class SubjectDisease(YAMLRoot):
    """
    ['Association between a C2M2 subject and a disease positively OR negatively clinically identified in that subject']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.SubjectDisease
    class_class_curie: ClassVar[str] = "ex:SubjectDisease"
    class_name: ClassVar[str] = "subject_disease"
    class_model_uri: ClassVar[URIRef] = EX.SubjectDisease

    subject_id_namespace: str = None
    subject_local_id: str = None
    association_type: Union[str, "AssociationTypeEnum"] = None
    disease: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject_id_namespace):
            self.MissingRequiredField("subject_id_namespace")
        if not isinstance(self.subject_id_namespace, str):
            self.subject_id_namespace = str(self.subject_id_namespace)

        if self._is_empty(self.subject_local_id):
            self.MissingRequiredField("subject_local_id")
        if not isinstance(self.subject_local_id, str):
            self.subject_local_id = str(self.subject_local_id)

        if self._is_empty(self.association_type):
            self.MissingRequiredField("association_type")
        if not isinstance(self.association_type, AssociationTypeEnum):
            self.association_type = AssociationTypeEnum(self.association_type)

        if self._is_empty(self.disease):
            self.MissingRequiredField("disease")
        if not isinstance(self.disease, str):
            self.disease = str(self.disease)

        super().__post_init__(**kwargs)


@dataclass
class CollectionDisease(YAMLRoot):
    """
    ['Association between a disease and a C2M2 collection containing experimental resources directly related to the
    study of that disease']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.CollectionDisease
    class_class_curie: ClassVar[str] = "ex:CollectionDisease"
    class_name: ClassVar[str] = "collection_disease"
    class_model_uri: ClassVar[URIRef] = EX.CollectionDisease

    collection_id_namespace: str = None
    collection_local_id: str = None
    disease: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.collection_id_namespace):
            self.MissingRequiredField("collection_id_namespace")
        if not isinstance(self.collection_id_namespace, str):
            self.collection_id_namespace = str(self.collection_id_namespace)

        if self._is_empty(self.collection_local_id):
            self.MissingRequiredField("collection_local_id")
        if not isinstance(self.collection_local_id, str):
            self.collection_local_id = str(self.collection_local_id)

        if self._is_empty(self.disease):
            self.MissingRequiredField("disease")
        if not isinstance(self.disease, str):
            self.disease = str(self.disease)

        super().__post_init__(**kwargs)


@dataclass
class CollectionPhenotype(YAMLRoot):
    """
    ['Association between a phenotype and a C2M2 collection containing experimental resources directly related to the
    study of that phenotype']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.CollectionPhenotype
    class_class_curie: ClassVar[str] = "ex:CollectionPhenotype"
    class_name: ClassVar[str] = "collection_phenotype"
    class_model_uri: ClassVar[URIRef] = EX.CollectionPhenotype

    collection_id_namespace: str = None
    collection_local_id: str = None
    phenotype: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.collection_id_namespace):
            self.MissingRequiredField("collection_id_namespace")
        if not isinstance(self.collection_id_namespace, str):
            self.collection_id_namespace = str(self.collection_id_namespace)

        if self._is_empty(self.collection_local_id):
            self.MissingRequiredField("collection_local_id")
        if not isinstance(self.collection_local_id, str):
            self.collection_local_id = str(self.collection_local_id)

        if self._is_empty(self.phenotype):
            self.MissingRequiredField("phenotype")
        if not isinstance(self.phenotype, str):
            self.phenotype = str(self.phenotype)

        super().__post_init__(**kwargs)


@dataclass
class CollectionGene(YAMLRoot):
    """
    ['Association between a gene and a C2M2 collection containing experimental resources directly related to the study
    of that gene']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.CollectionGene
    class_class_curie: ClassVar[str] = "ex:CollectionGene"
    class_name: ClassVar[str] = "collection_gene"
    class_model_uri: ClassVar[URIRef] = EX.CollectionGene

    collection_id_namespace: str = None
    collection_local_id: str = None
    gene: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.collection_id_namespace):
            self.MissingRequiredField("collection_id_namespace")
        if not isinstance(self.collection_id_namespace, str):
            self.collection_id_namespace = str(self.collection_id_namespace)

        if self._is_empty(self.collection_local_id):
            self.MissingRequiredField("collection_local_id")
        if not isinstance(self.collection_local_id, str):
            self.collection_local_id = str(self.collection_local_id)

        if self._is_empty(self.gene):
            self.MissingRequiredField("gene")
        if not isinstance(self.gene, str):
            self.gene = str(self.gene)

        super().__post_init__(**kwargs)


@dataclass
class CollectionCompound(YAMLRoot):
    """
    ['Association between a compound and a C2M2 collection containing experimental resources directly related to the
    study of that compound']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.CollectionCompound
    class_class_curie: ClassVar[str] = "ex:CollectionCompound"
    class_name: ClassVar[str] = "collection_compound"
    class_model_uri: ClassVar[URIRef] = EX.CollectionCompound

    collection_id_namespace: str = None
    collection_local_id: str = None
    compound: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.collection_id_namespace):
            self.MissingRequiredField("collection_id_namespace")
        if not isinstance(self.collection_id_namespace, str):
            self.collection_id_namespace = str(self.collection_id_namespace)

        if self._is_empty(self.collection_local_id):
            self.MissingRequiredField("collection_local_id")
        if not isinstance(self.collection_local_id, str):
            self.collection_local_id = str(self.collection_local_id)

        if self._is_empty(self.compound):
            self.MissingRequiredField("compound")
        if not isinstance(self.compound, str):
            self.compound = str(self.compound)

        super().__post_init__(**kwargs)


@dataclass
class CollectionSubstance(YAMLRoot):
    """
    ['Association between a substance and a C2M2 collection containing experimental resources directly related to the
    study of that substance']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.CollectionSubstance
    class_class_curie: ClassVar[str] = "ex:CollectionSubstance"
    class_name: ClassVar[str] = "collection_substance"
    class_model_uri: ClassVar[URIRef] = EX.CollectionSubstance

    collection_id_namespace: str = None
    collection_local_id: str = None
    substance: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.collection_id_namespace):
            self.MissingRequiredField("collection_id_namespace")
        if not isinstance(self.collection_id_namespace, str):
            self.collection_id_namespace = str(self.collection_id_namespace)

        if self._is_empty(self.collection_local_id):
            self.MissingRequiredField("collection_local_id")
        if not isinstance(self.collection_local_id, str):
            self.collection_local_id = str(self.collection_local_id)

        if self._is_empty(self.substance):
            self.MissingRequiredField("substance")
        if not isinstance(self.substance, str):
            self.substance = str(self.substance)

        super().__post_init__(**kwargs)


@dataclass
class CollectionTaxonomy(YAMLRoot):
    """
    ['Association between a taxon and a C2M2 collection containing experimental resources directly related to the
    study of that taxon']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.CollectionTaxonomy
    class_class_curie: ClassVar[str] = "ex:CollectionTaxonomy"
    class_name: ClassVar[str] = "collection_taxonomy"
    class_model_uri: ClassVar[URIRef] = EX.CollectionTaxonomy

    collection_id_namespace: str = None
    collection_local_id: str = None
    taxon: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.collection_id_namespace):
            self.MissingRequiredField("collection_id_namespace")
        if not isinstance(self.collection_id_namespace, str):
            self.collection_id_namespace = str(self.collection_id_namespace)

        if self._is_empty(self.collection_local_id):
            self.MissingRequiredField("collection_local_id")
        if not isinstance(self.collection_local_id, str):
            self.collection_local_id = str(self.collection_local_id)

        if self._is_empty(self.taxon):
            self.MissingRequiredField("taxon")
        if not isinstance(self.taxon, str):
            self.taxon = str(self.taxon)

        super().__post_init__(**kwargs)


@dataclass
class CollectionAnatomy(YAMLRoot):
    """
    ['Association between an UBERON anatomical term and a C2M2 collection containing experimental resources directly
    related to the study of the anatomical concept described by that term']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.CollectionAnatomy
    class_class_curie: ClassVar[str] = "ex:CollectionAnatomy"
    class_name: ClassVar[str] = "collection_anatomy"
    class_model_uri: ClassVar[URIRef] = EX.CollectionAnatomy

    collection_id_namespace: str = None
    collection_local_id: str = None
    anatomy: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.collection_id_namespace):
            self.MissingRequiredField("collection_id_namespace")
        if not isinstance(self.collection_id_namespace, str):
            self.collection_id_namespace = str(self.collection_id_namespace)

        if self._is_empty(self.collection_local_id):
            self.MissingRequiredField("collection_local_id")
        if not isinstance(self.collection_local_id, str):
            self.collection_local_id = str(self.collection_local_id)

        if self._is_empty(self.anatomy):
            self.MissingRequiredField("anatomy")
        if not isinstance(self.anatomy, str):
            self.anatomy = str(self.anatomy)

        super().__post_init__(**kwargs)


@dataclass
class CollectionProtein(YAMLRoot):
    """
    ['Association between a protein and a C2M2 collection containing experimental resources directly related to the
    study of that protein']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.CollectionProtein
    class_class_curie: ClassVar[str] = "ex:CollectionProtein"
    class_name: ClassVar[str] = "collection_protein"
    class_model_uri: ClassVar[URIRef] = EX.CollectionProtein

    collection_id_namespace: str = None
    collection_local_id: str = None
    protein: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.collection_id_namespace):
            self.MissingRequiredField("collection_id_namespace")
        if not isinstance(self.collection_id_namespace, str):
            self.collection_id_namespace = str(self.collection_id_namespace)

        if self._is_empty(self.collection_local_id):
            self.MissingRequiredField("collection_local_id")
        if not isinstance(self.collection_local_id, str):
            self.collection_local_id = str(self.collection_local_id)

        if self._is_empty(self.protein):
            self.MissingRequiredField("protein")
        if not isinstance(self.protein, str):
            self.protein = str(self.protein)

        super().__post_init__(**kwargs)


@dataclass
class SubjectPhenotype(YAMLRoot):
    """
    ['Association between a C2M2 subject and a phenotype positively OR negatively clinically identified for that
    subject']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.SubjectPhenotype
    class_class_curie: ClassVar[str] = "ex:SubjectPhenotype"
    class_name: ClassVar[str] = "subject_phenotype"
    class_model_uri: ClassVar[URIRef] = EX.SubjectPhenotype

    subject_id_namespace: str = None
    subject_local_id: str = None
    association_type: Union[str, "AssociationTypeEnum"] = None
    phenotype: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject_id_namespace):
            self.MissingRequiredField("subject_id_namespace")
        if not isinstance(self.subject_id_namespace, str):
            self.subject_id_namespace = str(self.subject_id_namespace)

        if self._is_empty(self.subject_local_id):
            self.MissingRequiredField("subject_local_id")
        if not isinstance(self.subject_local_id, str):
            self.subject_local_id = str(self.subject_local_id)

        if self._is_empty(self.association_type):
            self.MissingRequiredField("association_type")
        if not isinstance(self.association_type, AssociationTypeEnum):
            self.association_type = AssociationTypeEnum(self.association_type)

        if self._is_empty(self.phenotype):
            self.MissingRequiredField("phenotype")
        if not isinstance(self.phenotype, str):
            self.phenotype = str(self.phenotype)

        super().__post_init__(**kwargs)


@dataclass
class BiosampleSubstance(YAMLRoot):
    """
    ['Association between a C2M2 biosample and a PubChem substance experimentally associated with that biosample']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.BiosampleSubstance
    class_class_curie: ClassVar[str] = "ex:BiosampleSubstance"
    class_name: ClassVar[str] = "biosample_substance"
    class_model_uri: ClassVar[URIRef] = EX.BiosampleSubstance

    biosample_id_namespace: str = None
    biosample_local_id: str = None
    substance: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.biosample_id_namespace):
            self.MissingRequiredField("biosample_id_namespace")
        if not isinstance(self.biosample_id_namespace, str):
            self.biosample_id_namespace = str(self.biosample_id_namespace)

        if self._is_empty(self.biosample_local_id):
            self.MissingRequiredField("biosample_local_id")
        if not isinstance(self.biosample_local_id, str):
            self.biosample_local_id = str(self.biosample_local_id)

        if self._is_empty(self.substance):
            self.MissingRequiredField("substance")
        if not isinstance(self.substance, str):
            self.substance = str(self.substance)

        super().__post_init__(**kwargs)


@dataclass
class SubjectSubstance(YAMLRoot):
    """
    ['Association between a C2M2 subject and a PubChem substance experimentally associated with that subject']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.SubjectSubstance
    class_class_curie: ClassVar[str] = "ex:SubjectSubstance"
    class_name: ClassVar[str] = "subject_substance"
    class_model_uri: ClassVar[URIRef] = EX.SubjectSubstance

    subject_id_namespace: str = None
    subject_local_id: str = None
    substance: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject_id_namespace):
            self.MissingRequiredField("subject_id_namespace")
        if not isinstance(self.subject_id_namespace, str):
            self.subject_id_namespace = str(self.subject_id_namespace)

        if self._is_empty(self.subject_local_id):
            self.MissingRequiredField("subject_local_id")
        if not isinstance(self.subject_local_id, str):
            self.subject_local_id = str(self.subject_local_id)

        if self._is_empty(self.substance):
            self.MissingRequiredField("substance")
        if not isinstance(self.substance, str):
            self.substance = str(self.substance)

        super().__post_init__(**kwargs)


@dataclass
class BiosampleGene(YAMLRoot):
    """
    ['Association between a C2M2 biosample and an Ensembl gene especially relevant to it']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.BiosampleGene
    class_class_curie: ClassVar[str] = "ex:BiosampleGene"
    class_name: ClassVar[str] = "biosample_gene"
    class_model_uri: ClassVar[URIRef] = EX.BiosampleGene

    biosample_id_namespace: str = None
    biosample_local_id: str = None
    gene: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.biosample_id_namespace):
            self.MissingRequiredField("biosample_id_namespace")
        if not isinstance(self.biosample_id_namespace, str):
            self.biosample_id_namespace = str(self.biosample_id_namespace)

        if self._is_empty(self.biosample_local_id):
            self.MissingRequiredField("biosample_local_id")
        if not isinstance(self.biosample_local_id, str):
            self.biosample_local_id = str(self.biosample_local_id)

        if self._is_empty(self.gene):
            self.MissingRequiredField("gene")
        if not isinstance(self.gene, str):
            self.gene = str(self.gene)

        super().__post_init__(**kwargs)


@dataclass
class PhenotypeGene(YAMLRoot):
    """
    ['Association between a Human Phenotype Ontology term and an Ensembl gene especially relevant to it']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.PhenotypeGene
    class_class_curie: ClassVar[str] = "ex:PhenotypeGene"
    class_name: ClassVar[str] = "phenotype_gene"
    class_model_uri: ClassVar[URIRef] = EX.PhenotypeGene

    phenotype: str = None
    gene: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.phenotype):
            self.MissingRequiredField("phenotype")
        if not isinstance(self.phenotype, str):
            self.phenotype = str(self.phenotype)

        if self._is_empty(self.gene):
            self.MissingRequiredField("gene")
        if not isinstance(self.gene, str):
            self.gene = str(self.gene)

        super().__post_init__(**kwargs)


@dataclass
class PhenotypeDisease(YAMLRoot):
    """
    ['Association between a Human Phenotype Ontology term and a Disease Ontology term identifying a disease especially
    relevant to it']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.PhenotypeDisease
    class_class_curie: ClassVar[str] = "ex:PhenotypeDisease"
    class_name: ClassVar[str] = "phenotype_disease"
    class_model_uri: ClassVar[URIRef] = EX.PhenotypeDisease

    phenotype: str = None
    disease: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.phenotype):
            self.MissingRequiredField("phenotype")
        if not isinstance(self.phenotype, str):
            self.phenotype = str(self.phenotype)

        if self._is_empty(self.disease):
            self.MissingRequiredField("disease")
        if not isinstance(self.disease, str):
            self.disease = str(self.disease)

        super().__post_init__(**kwargs)


@dataclass
class SubjectRace(YAMLRoot):
    """
    ['Identification of a C2M2 subject with one or more self-selected races']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.SubjectRace
    class_class_curie: ClassVar[str] = "ex:SubjectRace"
    class_name: ClassVar[str] = "subject_race"
    class_model_uri: ClassVar[URIRef] = EX.SubjectRace

    subject_id_namespace: str = None
    subject_local_id: str = None
    race: Optional[Union[str, "RaceEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject_id_namespace):
            self.MissingRequiredField("subject_id_namespace")
        if not isinstance(self.subject_id_namespace, str):
            self.subject_id_namespace = str(self.subject_id_namespace)

        if self._is_empty(self.subject_local_id):
            self.MissingRequiredField("subject_local_id")
        if not isinstance(self.subject_local_id, str):
            self.subject_local_id = str(self.subject_local_id)

        if self.race is not None and not isinstance(self.race, RaceEnum):
            self.race = RaceEnum(self.race)

        super().__post_init__(**kwargs)


@dataclass
class SubjectRoleTaxonomy(YAMLRoot):
    """
    ["Trinary association linking IDs representing (1) a subject, (2) a subject_role (a named organism-level
    constituent component of a subject, like 'host', 'pathogen', 'endosymbiont', 'taxon detected inside a microbiome
    subject', etc.) and (3) a taxonomic label (which is hereby assigned to this particular subject_role within this
    particular subject)"]
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.SubjectRoleTaxonomy
    class_class_curie: ClassVar[str] = "ex:SubjectRoleTaxonomy"
    class_name: ClassVar[str] = "subject_role_taxonomy"
    class_model_uri: ClassVar[URIRef] = EX.SubjectRoleTaxonomy

    subject_id_namespace: str = None
    subject_local_id: str = None
    role_id: Union[str, "RoleIdEnum"] = None
    taxonomy_id: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject_id_namespace):
            self.MissingRequiredField("subject_id_namespace")
        if not isinstance(self.subject_id_namespace, str):
            self.subject_id_namespace = str(self.subject_id_namespace)

        if self._is_empty(self.subject_local_id):
            self.MissingRequiredField("subject_local_id")
        if not isinstance(self.subject_local_id, str):
            self.subject_local_id = str(self.subject_local_id)

        if self._is_empty(self.role_id):
            self.MissingRequiredField("role_id")
        if not isinstance(self.role_id, RoleIdEnum):
            self.role_id = RoleIdEnum(self.role_id)

        if self._is_empty(self.taxonomy_id):
            self.MissingRequiredField("taxonomy_id")
        if not isinstance(self.taxonomy_id, str):
            self.taxonomy_id = str(self.taxonomy_id)

        super().__post_init__(**kwargs)


@dataclass
class AssayType(YAMLRoot):
    """
    ['List of Ontology for Biomedical Investigations (OBI) CV terms used to describe types of experiment that generate
    C2M2 biosamples or results stored in C2M2 files']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.AssayType
    class_class_curie: ClassVar[str] = "ex:AssayType"
    class_name: ClassVar[str] = "assay_type"
    class_model_uri: ClassVar[URIRef] = EX.AssayType

    id: str = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        super().__post_init__(**kwargs)


@dataclass
class AnalysisType(YAMLRoot):
    """
    ['List of Ontology for Biomedical Investigations (OBI) CV terms used to describe analytic methods that generate
    C2M2 files']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.AnalysisType
    class_class_curie: ClassVar[str] = "ex:AnalysisType"
    class_name: ClassVar[str] = "analysis_type"
    class_model_uri: ClassVar[URIRef] = EX.AnalysisType

    id: str = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        super().__post_init__(**kwargs)


@dataclass
class NcbiTaxonomy(YAMLRoot):
    """
    ['List of NCBI Taxonomy Database IDs identifying taxa used to describe C2M2 subjects']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.NcbiTaxonomy
    class_class_curie: ClassVar[str] = "ex:NcbiTaxonomy"
    class_name: ClassVar[str] = "ncbi_taxonomy"
    class_model_uri: ClassVar[URIRef] = EX.NcbiTaxonomy

    id: str = None
    clade: str = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.clade):
            self.MissingRequiredField("clade")
        if not isinstance(self.clade, str):
            self.clade = str(self.clade)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        super().__post_init__(**kwargs)


@dataclass
class Anatomy(YAMLRoot):
    """
    ['List of Uber-anatomy ontology (UBERON) CV terms used to locate the origin of a C2M2 biosample within the
    physiology of its source or host organism']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.Anatomy
    class_class_curie: ClassVar[str] = "ex:Anatomy"
    class_name: ClassVar[str] = "anatomy"
    class_model_uri: ClassVar[URIRef] = EX.Anatomy

    id: str = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        super().__post_init__(**kwargs)


@dataclass
class FileFormat(YAMLRoot):
    """
    ["List of EDAM CV 'format:' terms used to describe formats of C2M2 files"]
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.FileFormat
    class_class_curie: ClassVar[str] = "ex:FileFormat"
    class_name: ClassVar[str] = "file_format"
    class_model_uri: ClassVar[URIRef] = EX.FileFormat

    id: str = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        super().__post_init__(**kwargs)


@dataclass
class DataType(YAMLRoot):
    """
    ["List of EDAM CV 'data:' terms used to describe data in C2M2 files"]
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.DataType
    class_class_curie: ClassVar[str] = "ex:DataType"
    class_name: ClassVar[str] = "data_type"
    class_model_uri: ClassVar[URIRef] = EX.DataType

    id: str = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        super().__post_init__(**kwargs)


@dataclass
class Disease(YAMLRoot):
    """
    ['List of Disease Ontology terms used to describe diseases recorded in association with C2M2 subjects or
    biosamples']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.Disease
    class_class_curie: ClassVar[str] = "ex:Disease"
    class_name: ClassVar[str] = "disease"
    class_model_uri: ClassVar[URIRef] = EX.Disease

    id: str = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        super().__post_init__(**kwargs)


@dataclass
class Phenotype(YAMLRoot):
    """
    ['List of Human Phenotype Ontology terms used to describe phenotypes recorded in association with C2M2 subjects']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.Phenotype
    class_class_curie: ClassVar[str] = "ex:Phenotype"
    class_name: ClassVar[str] = "phenotype"
    class_model_uri: ClassVar[URIRef] = EX.Phenotype

    id: str = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        super().__post_init__(**kwargs)


@dataclass
class Compound(YAMLRoot):
    """
    ["List of (i) GlyTouCan terms or (ii) PubChem 'compound' terms (normalized chemical structures) referenced in this
    submission; (ii) will include all PubChem 'compound' terms associated with any PubChem 'substance' terms (specific
    formulations of chemical materials) directly referenced in this submission, in addition to any 'compound' terms
    directly referenced"]
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.Compound
    class_class_curie: ClassVar[str] = "ex:Compound"
    class_name: ClassVar[str] = "compound"
    class_model_uri: ClassVar[URIRef] = EX.Compound

    id: str = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        super().__post_init__(**kwargs)


@dataclass
class Substance(YAMLRoot):
    """
    ["List of PubChem 'substance' terms (specific formulations of chemical materials) directly referenced in this C2M2
    submission"]
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.Substance
    class_class_curie: ClassVar[str] = "ex:Substance"
    class_name: ClassVar[str] = "substance"
    class_model_uri: ClassVar[URIRef] = EX.Substance

    id: str = None
    compound: str = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.compound):
            self.MissingRequiredField("compound")
        if not isinstance(self.compound, str):
            self.compound = str(self.compound)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        super().__post_init__(**kwargs)


@dataclass
class Gene(YAMLRoot):
    """
    ['List of Ensembl genes directly referenced in this C2M2 submission']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.Gene
    class_class_curie: ClassVar[str] = "ex:Gene"
    class_name: ClassVar[str] = "gene"
    class_model_uri: ClassVar[URIRef] = EX.Gene

    id: str = None
    organism: str = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.organism):
            self.MissingRequiredField("organism")
        if not isinstance(self.organism, str):
            self.organism = str(self.organism)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        super().__post_init__(**kwargs)


@dataclass
class Protein(YAMLRoot):
    """
    ['List of UniProtKB proteins directly referenced in this C2M2 submission']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.Protein
    class_class_curie: ClassVar[str] = "ex:Protein"
    class_name: ClassVar[str] = "protein"
    class_model_uri: ClassVar[URIRef] = EX.Protein

    id: str = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()
    organism: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        if self.organism is not None and not isinstance(self.organism, str):
            self.organism = str(self.organism)

        super().__post_init__(**kwargs)


@dataclass
class ProteinGene(YAMLRoot):
    """
    ['Association between a UniProtKB protein term and an Ensembl term identifying a gene encoding that protein']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.ProteinGene
    class_class_curie: ClassVar[str] = "ex:ProteinGene"
    class_name: ClassVar[str] = "protein_gene"
    class_model_uri: ClassVar[URIRef] = EX.ProteinGene

    protein: str = None
    gene: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.protein):
            self.MissingRequiredField("protein")
        if not isinstance(self.protein, str):
            self.protein = str(self.protein)

        if self._is_empty(self.gene):
            self.MissingRequiredField("gene")
        if not isinstance(self.gene, str):
            self.gene = str(self.gene)

        super().__post_init__(**kwargs)


@dataclass
class IdNamespace(YAMLRoot):
    """
    ['A table listing identifier namespaces registered by the DCC submitting this C2M2 instance']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.IdNamespace
    class_class_curie: ClassVar[str] = "ex:IdNamespace"
    class_name: ClassVar[str] = "id_namespace"
    class_model_uri: ClassVar[URIRef] = EX.IdNamespace

    id: str = None
    abbreviation: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.abbreviation is not None and not isinstance(self.abbreviation, str):
            self.abbreviation = str(self.abbreviation)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


# Enumerations
class GranularityEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="GranularityEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0",
                PermissibleValue(text="0",
                                 meaning=CFDE_SUBJECT_GRANULARITY["0"]) )
        setattr(cls, "1",
                PermissibleValue(text="1",
                                 meaning=CFDE_SUBJECT_GRANULARITY["1"]) )
        setattr(cls, "2",
                PermissibleValue(text="2",
                                 meaning=CFDE_SUBJECT_GRANULARITY["2"]) )
        setattr(cls, "3",
                PermissibleValue(text="3",
                                 meaning=CFDE_SUBJECT_GRANULARITY["3"]) )
        setattr(cls, "4",
                PermissibleValue(text="4",
                                 meaning=CFDE_SUBJECT_GRANULARITY["4"]) )
        setattr(cls, "5",
                PermissibleValue(text="5",
                                 meaning=CFDE_SUBJECT_GRANULARITY["5"]) )

class SexEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="SexEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0",
                PermissibleValue(text="0",
                                 meaning=CFDE_SUBJECT_SEX["0"]) )
        setattr(cls, "1",
                PermissibleValue(text="1",
                                 meaning=CFDE_SUBJECT_SEX["1"]) )
        setattr(cls, "2",
                PermissibleValue(text="2",
                                 meaning=CFDE_SUBJECT_SEX["2"]) )
        setattr(cls, "3",
                PermissibleValue(text="3",
                                 meaning=CFDE_SUBJECT_SEX["3"]) )
        setattr(cls, "4",
                PermissibleValue(text="4",
                                 meaning=CFDE_SUBJECT_SEX["4"]) )
        setattr(cls, "5",
                PermissibleValue(text="5",
                                 meaning=CFDE_SUBJECT_SEX["5"]) )

class EthnicityEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EthnicityEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0",
                PermissibleValue(text="0",
                                 meaning=CFDE_SUBJECT_ETHNICITY["0"]) )
        setattr(cls, "1",
                PermissibleValue(text="1",
                                 meaning=CFDE_SUBJECT_ETHNICITY["1"]) )

class AssociationTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AssociationTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0",
                PermissibleValue(text="0",
                                 meaning=CFDE_PHENOTYPE_ASSOCIATION_TYPE["0"]) )
        setattr(cls, "1",
                PermissibleValue(text="1",
                                 meaning=CFDE_PHENOTYPE_ASSOCIATION_TYPE["1"]) )

class RaceEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="RaceEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0",
                PermissibleValue(text="0",
                                 meaning=CFDE_SUBJECT_RACE["0"]) )
        setattr(cls, "1",
                PermissibleValue(text="1",
                                 meaning=CFDE_SUBJECT_RACE["1"]) )
        setattr(cls, "2",
                PermissibleValue(text="2",
                                 meaning=CFDE_SUBJECT_RACE["2"]) )
        setattr(cls, "3",
                PermissibleValue(text="3",
                                 meaning=CFDE_SUBJECT_RACE["3"]) )
        setattr(cls, "4",
                PermissibleValue(text="4",
                                 meaning=CFDE_SUBJECT_RACE["4"]) )

class RoleIdEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="RoleIdEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0",
                PermissibleValue(text="0",
                                 meaning=CFDE_SUBJECT_ROLE["0"]) )
        setattr(cls, "1",
                PermissibleValue(text="1",
                                 meaning=CFDE_SUBJECT_ROLE["1"]) )
        setattr(cls, "2",
                PermissibleValue(text="2",
                                 meaning=CFDE_SUBJECT_ROLE["2"]) )
        setattr(cls, "3",
                PermissibleValue(text="3",
                                 meaning=CFDE_SUBJECT_ROLE["3"]) )
        setattr(cls, "4",
                PermissibleValue(text="4",
                                 meaning=CFDE_SUBJECT_ROLE["4"]) )
        setattr(cls, "5",
                PermissibleValue(text="5",
                                 meaning=CFDE_SUBJECT_ROLE["5"]) )
        setattr(cls, "6",
                PermissibleValue(text="6",
                                 meaning=CFDE_SUBJECT_ROLE["6"]) )
        setattr(cls, "7",
                PermissibleValue(text="7",
                                 meaning=CFDE_SUBJECT_ROLE["7"]) )

# Slots
class slots:
    pass

slots.file__id_namespace = Slot(uri=EX.id_namespace, name="file__id_namespace", curie=EX.curie('id_namespace'),
                   model_uri=EX.file__id_namespace, domain=None, range=str)

slots.file__local_id = Slot(uri=EX.local_id, name="file__local_id", curie=EX.curie('local_id'),
                   model_uri=EX.file__local_id, domain=None, range=str)

slots.file__project_id_namespace = Slot(uri=EX.project_id_namespace, name="file__project_id_namespace", curie=EX.curie('project_id_namespace'),
                   model_uri=EX.file__project_id_namespace, domain=None, range=str)

slots.file__project_local_id = Slot(uri=EX.project_local_id, name="file__project_local_id", curie=EX.curie('project_local_id'),
                   model_uri=EX.file__project_local_id, domain=None, range=str)

slots.file__persistent_id = Slot(uri=EX.persistent_id, name="file__persistent_id", curie=EX.curie('persistent_id'),
                   model_uri=EX.file__persistent_id, domain=None, range=Optional[str])

slots.file__creation_time = Slot(uri=EX.creation_time, name="file__creation_time", curie=EX.curie('creation_time'),
                   model_uri=EX.file__creation_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.file__size_in_bytes = Slot(uri=EX.size_in_bytes, name="file__size_in_bytes", curie=EX.curie('size_in_bytes'),
                   model_uri=EX.file__size_in_bytes, domain=None, range=Optional[int])

slots.file__uncompressed_size_in_bytes = Slot(uri=EX.uncompressed_size_in_bytes, name="file__uncompressed_size_in_bytes", curie=EX.curie('uncompressed_size_in_bytes'),
                   model_uri=EX.file__uncompressed_size_in_bytes, domain=None, range=Optional[int])

slots.file__sha256 = Slot(uri=EX.sha256, name="file__sha256", curie=EX.curie('sha256'),
                   model_uri=EX.file__sha256, domain=None, range=Optional[str])

slots.file__md5 = Slot(uri=EX.md5, name="file__md5", curie=EX.curie('md5'),
                   model_uri=EX.file__md5, domain=None, range=Optional[str])

slots.file__filename = Slot(uri=EX.filename, name="file__filename", curie=EX.curie('filename'),
                   model_uri=EX.file__filename, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[^/\:]+$'))

slots.file__file_format = Slot(uri=EX.file_format, name="file__file_format", curie=EX.curie('file_format'),
                   model_uri=EX.file__file_format, domain=None, range=Optional[str])

slots.file__compression_format = Slot(uri=EX.compression_format, name="file__compression_format", curie=EX.curie('compression_format'),
                   model_uri=EX.file__compression_format, domain=None, range=Optional[str])

slots.file__data_type = Slot(uri=EX.data_type, name="file__data_type", curie=EX.curie('data_type'),
                   model_uri=EX.file__data_type, domain=None, range=Optional[str])

slots.file__assay_type = Slot(uri=EX.assay_type, name="file__assay_type", curie=EX.curie('assay_type'),
                   model_uri=EX.file__assay_type, domain=None, range=Optional[str])

slots.file__analysis_type = Slot(uri=EX.analysis_type, name="file__analysis_type", curie=EX.curie('analysis_type'),
                   model_uri=EX.file__analysis_type, domain=None, range=Optional[str])

slots.file__mime_type = Slot(uri=EX.mime_type, name="file__mime_type", curie=EX.curie('mime_type'),
                   model_uri=EX.file__mime_type, domain=None, range=Optional[str])

slots.file__bundle_collection_id_namespace = Slot(uri=EX.bundle_collection_id_namespace, name="file__bundle_collection_id_namespace", curie=EX.curie('bundle_collection_id_namespace'),
                   model_uri=EX.file__bundle_collection_id_namespace, domain=None, range=Optional[str])

slots.file__bundle_collection_local_id = Slot(uri=EX.bundle_collection_local_id, name="file__bundle_collection_local_id", curie=EX.curie('bundle_collection_local_id'),
                   model_uri=EX.file__bundle_collection_local_id, domain=None, range=Optional[str])

slots.file__dbgap_study_id = Slot(uri=EX.dbgap_study_id, name="file__dbgap_study_id", curie=EX.curie('dbgap_study_id'),
                   model_uri=EX.file__dbgap_study_id, domain=None, range=Optional[str])

slots.biosample__id_namespace = Slot(uri=EX.id_namespace, name="biosample__id_namespace", curie=EX.curie('id_namespace'),
                   model_uri=EX.biosample__id_namespace, domain=None, range=str)

slots.biosample__local_id = Slot(uri=EX.local_id, name="biosample__local_id", curie=EX.curie('local_id'),
                   model_uri=EX.biosample__local_id, domain=None, range=str)

slots.biosample__project_id_namespace = Slot(uri=EX.project_id_namespace, name="biosample__project_id_namespace", curie=EX.curie('project_id_namespace'),
                   model_uri=EX.biosample__project_id_namespace, domain=None, range=str)

slots.biosample__project_local_id = Slot(uri=EX.project_local_id, name="biosample__project_local_id", curie=EX.curie('project_local_id'),
                   model_uri=EX.biosample__project_local_id, domain=None, range=str)

slots.biosample__persistent_id = Slot(uri=EX.persistent_id, name="biosample__persistent_id", curie=EX.curie('persistent_id'),
                   model_uri=EX.biosample__persistent_id, domain=None, range=Optional[str])

slots.biosample__creation_time = Slot(uri=EX.creation_time, name="biosample__creation_time", curie=EX.curie('creation_time'),
                   model_uri=EX.biosample__creation_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.biosample__assay_type = Slot(uri=EX.assay_type, name="biosample__assay_type", curie=EX.curie('assay_type'),
                   model_uri=EX.biosample__assay_type, domain=None, range=Optional[str])

slots.biosample__anatomy = Slot(uri=EX.anatomy, name="biosample__anatomy", curie=EX.curie('anatomy'),
                   model_uri=EX.biosample__anatomy, domain=None, range=Optional[str])

slots.subject__id_namespace = Slot(uri=EX.id_namespace, name="subject__id_namespace", curie=EX.curie('id_namespace'),
                   model_uri=EX.subject__id_namespace, domain=None, range=str)

slots.subject__local_id = Slot(uri=EX.local_id, name="subject__local_id", curie=EX.curie('local_id'),
                   model_uri=EX.subject__local_id, domain=None, range=str)

slots.subject__project_id_namespace = Slot(uri=EX.project_id_namespace, name="subject__project_id_namespace", curie=EX.curie('project_id_namespace'),
                   model_uri=EX.subject__project_id_namespace, domain=None, range=str)

slots.subject__project_local_id = Slot(uri=EX.project_local_id, name="subject__project_local_id", curie=EX.curie('project_local_id'),
                   model_uri=EX.subject__project_local_id, domain=None, range=str)

slots.subject__persistent_id = Slot(uri=EX.persistent_id, name="subject__persistent_id", curie=EX.curie('persistent_id'),
                   model_uri=EX.subject__persistent_id, domain=None, range=Optional[str])

slots.subject__creation_time = Slot(uri=EX.creation_time, name="subject__creation_time", curie=EX.curie('creation_time'),
                   model_uri=EX.subject__creation_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.subject__granularity = Slot(uri=EX.granularity, name="subject__granularity", curie=EX.curie('granularity'),
                   model_uri=EX.subject__granularity, domain=None, range=Union[str, "GranularityEnum"])

slots.subject__sex = Slot(uri=EX.sex, name="subject__sex", curie=EX.curie('sex'),
                   model_uri=EX.subject__sex, domain=None, range=Optional[Union[str, "SexEnum"]])

slots.subject__ethnicity = Slot(uri=EX.ethnicity, name="subject__ethnicity", curie=EX.curie('ethnicity'),
                   model_uri=EX.subject__ethnicity, domain=None, range=Optional[Union[str, "EthnicityEnum"]])

slots.subject__age_at_enrollment = Slot(uri=EX.age_at_enrollment, name="subject__age_at_enrollment", curie=EX.curie('age_at_enrollment'),
                   model_uri=EX.subject__age_at_enrollment, domain=None, range=Optional[Decimal])

slots.dcc__id = Slot(uri=EX.id, name="dcc__id", curie=EX.curie('id'),
                   model_uri=EX.dcc__id, domain=None, range=str)

slots.dcc__dcc_name = Slot(uri=EX.dcc_name, name="dcc__dcc_name", curie=EX.curie('dcc_name'),
                   model_uri=EX.dcc__dcc_name, domain=None, range=str)

slots.dcc__dcc_abbreviation = Slot(uri=EX.dcc_abbreviation, name="dcc__dcc_abbreviation", curie=EX.curie('dcc_abbreviation'),
                   model_uri=EX.dcc__dcc_abbreviation, domain=None, range=str,
                   pattern=re.compile(r'^[a-zA-Z0-9_]+$'))

slots.dcc__dcc_description = Slot(uri=EX.dcc_description, name="dcc__dcc_description", curie=EX.curie('dcc_description'),
                   model_uri=EX.dcc__dcc_description, domain=None, range=Optional[str])

slots.dcc__contact_email = Slot(uri=EX.contact_email, name="dcc__contact_email", curie=EX.curie('contact_email'),
                   model_uri=EX.dcc__contact_email, domain=None, range=str)

slots.dcc__contact_name = Slot(uri=EX.contact_name, name="dcc__contact_name", curie=EX.curie('contact_name'),
                   model_uri=EX.dcc__contact_name, domain=None, range=str)

slots.dcc__dcc_url = Slot(uri=EX.dcc_url, name="dcc__dcc_url", curie=EX.curie('dcc_url'),
                   model_uri=EX.dcc__dcc_url, domain=None, range=str)

slots.dcc__project_id_namespace = Slot(uri=EX.project_id_namespace, name="dcc__project_id_namespace", curie=EX.curie('project_id_namespace'),
                   model_uri=EX.dcc__project_id_namespace, domain=None, range=str)

slots.dcc__project_local_id = Slot(uri=EX.project_local_id, name="dcc__project_local_id", curie=EX.curie('project_local_id'),
                   model_uri=EX.dcc__project_local_id, domain=None, range=str)

slots.project__id_namespace = Slot(uri=EX.id_namespace, name="project__id_namespace", curie=EX.curie('id_namespace'),
                   model_uri=EX.project__id_namespace, domain=None, range=str)

slots.project__local_id = Slot(uri=EX.local_id, name="project__local_id", curie=EX.curie('local_id'),
                   model_uri=EX.project__local_id, domain=None, range=str)

slots.project__persistent_id = Slot(uri=EX.persistent_id, name="project__persistent_id", curie=EX.curie('persistent_id'),
                   model_uri=EX.project__persistent_id, domain=None, range=Optional[str])

slots.project__creation_time = Slot(uri=EX.creation_time, name="project__creation_time", curie=EX.curie('creation_time'),
                   model_uri=EX.project__creation_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.project__abbreviation = Slot(uri=EX.abbreviation, name="project__abbreviation", curie=EX.curie('abbreviation'),
                   model_uri=EX.project__abbreviation, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-zA-Z0-9_]+$'))

slots.project__description = Slot(uri=EX.description, name="project__description", curie=EX.curie('description'),
                   model_uri=EX.project__description, domain=None, range=Optional[str])

slots.projectInProject__parent_project_id_namespace = Slot(uri=EX.parent_project_id_namespace, name="projectInProject__parent_project_id_namespace", curie=EX.curie('parent_project_id_namespace'),
                   model_uri=EX.projectInProject__parent_project_id_namespace, domain=None, range=str)

slots.projectInProject__parent_project_local_id = Slot(uri=EX.parent_project_local_id, name="projectInProject__parent_project_local_id", curie=EX.curie('parent_project_local_id'),
                   model_uri=EX.projectInProject__parent_project_local_id, domain=None, range=str)

slots.projectInProject__child_project_id_namespace = Slot(uri=EX.child_project_id_namespace, name="projectInProject__child_project_id_namespace", curie=EX.curie('child_project_id_namespace'),
                   model_uri=EX.projectInProject__child_project_id_namespace, domain=None, range=str)

slots.projectInProject__child_project_local_id = Slot(uri=EX.child_project_local_id, name="projectInProject__child_project_local_id", curie=EX.curie('child_project_local_id'),
                   model_uri=EX.projectInProject__child_project_local_id, domain=None, range=str)

slots.collection__id_namespace = Slot(uri=EX.id_namespace, name="collection__id_namespace", curie=EX.curie('id_namespace'),
                   model_uri=EX.collection__id_namespace, domain=None, range=str)

slots.collection__local_id = Slot(uri=EX.local_id, name="collection__local_id", curie=EX.curie('local_id'),
                   model_uri=EX.collection__local_id, domain=None, range=str)

slots.collection__persistent_id = Slot(uri=EX.persistent_id, name="collection__persistent_id", curie=EX.curie('persistent_id'),
                   model_uri=EX.collection__persistent_id, domain=None, range=Optional[str])

slots.collection__creation_time = Slot(uri=EX.creation_time, name="collection__creation_time", curie=EX.curie('creation_time'),
                   model_uri=EX.collection__creation_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.collection__abbreviation = Slot(uri=EX.abbreviation, name="collection__abbreviation", curie=EX.curie('abbreviation'),
                   model_uri=EX.collection__abbreviation, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-zA-Z0-9_]+$'))

slots.collection__description = Slot(uri=EX.description, name="collection__description", curie=EX.curie('description'),
                   model_uri=EX.collection__description, domain=None, range=Optional[str])

slots.collection__has_time_series_data = Slot(uri=EX.has_time_series_data, name="collection__has_time_series_data", curie=EX.curie('has_time_series_data'),
                   model_uri=EX.collection__has_time_series_data, domain=None, range=Optional[Union[bool, Bool]])

slots.collectionInCollection__superset_collection_id_namespace = Slot(uri=EX.superset_collection_id_namespace, name="collectionInCollection__superset_collection_id_namespace", curie=EX.curie('superset_collection_id_namespace'),
                   model_uri=EX.collectionInCollection__superset_collection_id_namespace, domain=None, range=str)

slots.collectionInCollection__superset_collection_local_id = Slot(uri=EX.superset_collection_local_id, name="collectionInCollection__superset_collection_local_id", curie=EX.curie('superset_collection_local_id'),
                   model_uri=EX.collectionInCollection__superset_collection_local_id, domain=None, range=str)

slots.collectionInCollection__subset_collection_id_namespace = Slot(uri=EX.subset_collection_id_namespace, name="collectionInCollection__subset_collection_id_namespace", curie=EX.curie('subset_collection_id_namespace'),
                   model_uri=EX.collectionInCollection__subset_collection_id_namespace, domain=None, range=str)

slots.collectionInCollection__subset_collection_local_id = Slot(uri=EX.subset_collection_local_id, name="collectionInCollection__subset_collection_local_id", curie=EX.curie('subset_collection_local_id'),
                   model_uri=EX.collectionInCollection__subset_collection_local_id, domain=None, range=str)

slots.fileDescribesCollection__file_id_namespace = Slot(uri=EX.file_id_namespace, name="fileDescribesCollection__file_id_namespace", curie=EX.curie('file_id_namespace'),
                   model_uri=EX.fileDescribesCollection__file_id_namespace, domain=None, range=str)

slots.fileDescribesCollection__file_local_id = Slot(uri=EX.file_local_id, name="fileDescribesCollection__file_local_id", curie=EX.curie('file_local_id'),
                   model_uri=EX.fileDescribesCollection__file_local_id, domain=None, range=str)

slots.fileDescribesCollection__collection_id_namespace = Slot(uri=EX.collection_id_namespace, name="fileDescribesCollection__collection_id_namespace", curie=EX.curie('collection_id_namespace'),
                   model_uri=EX.fileDescribesCollection__collection_id_namespace, domain=None, range=str)

slots.fileDescribesCollection__collection_local_id = Slot(uri=EX.collection_local_id, name="fileDescribesCollection__collection_local_id", curie=EX.curie('collection_local_id'),
                   model_uri=EX.fileDescribesCollection__collection_local_id, domain=None, range=str)

slots.collectionDefinedByProject__collection_id_namespace = Slot(uri=EX.collection_id_namespace, name="collectionDefinedByProject__collection_id_namespace", curie=EX.curie('collection_id_namespace'),
                   model_uri=EX.collectionDefinedByProject__collection_id_namespace, domain=None, range=str)

slots.collectionDefinedByProject__collection_local_id = Slot(uri=EX.collection_local_id, name="collectionDefinedByProject__collection_local_id", curie=EX.curie('collection_local_id'),
                   model_uri=EX.collectionDefinedByProject__collection_local_id, domain=None, range=str)

slots.collectionDefinedByProject__project_id_namespace = Slot(uri=EX.project_id_namespace, name="collectionDefinedByProject__project_id_namespace", curie=EX.curie('project_id_namespace'),
                   model_uri=EX.collectionDefinedByProject__project_id_namespace, domain=None, range=str)

slots.collectionDefinedByProject__project_local_id = Slot(uri=EX.project_local_id, name="collectionDefinedByProject__project_local_id", curie=EX.curie('project_local_id'),
                   model_uri=EX.collectionDefinedByProject__project_local_id, domain=None, range=str)

slots.fileInCollection__file_id_namespace = Slot(uri=EX.file_id_namespace, name="fileInCollection__file_id_namespace", curie=EX.curie('file_id_namespace'),
                   model_uri=EX.fileInCollection__file_id_namespace, domain=None, range=str)

slots.fileInCollection__file_local_id = Slot(uri=EX.file_local_id, name="fileInCollection__file_local_id", curie=EX.curie('file_local_id'),
                   model_uri=EX.fileInCollection__file_local_id, domain=None, range=str)

slots.fileInCollection__collection_id_namespace = Slot(uri=EX.collection_id_namespace, name="fileInCollection__collection_id_namespace", curie=EX.curie('collection_id_namespace'),
                   model_uri=EX.fileInCollection__collection_id_namespace, domain=None, range=str)

slots.fileInCollection__collection_local_id = Slot(uri=EX.collection_local_id, name="fileInCollection__collection_local_id", curie=EX.curie('collection_local_id'),
                   model_uri=EX.fileInCollection__collection_local_id, domain=None, range=str)

slots.biosampleInCollection__biosample_id_namespace = Slot(uri=EX.biosample_id_namespace, name="biosampleInCollection__biosample_id_namespace", curie=EX.curie('biosample_id_namespace'),
                   model_uri=EX.biosampleInCollection__biosample_id_namespace, domain=None, range=str)

slots.biosampleInCollection__biosample_local_id = Slot(uri=EX.biosample_local_id, name="biosampleInCollection__biosample_local_id", curie=EX.curie('biosample_local_id'),
                   model_uri=EX.biosampleInCollection__biosample_local_id, domain=None, range=str)

slots.biosampleInCollection__collection_id_namespace = Slot(uri=EX.collection_id_namespace, name="biosampleInCollection__collection_id_namespace", curie=EX.curie('collection_id_namespace'),
                   model_uri=EX.biosampleInCollection__collection_id_namespace, domain=None, range=str)

slots.biosampleInCollection__collection_local_id = Slot(uri=EX.collection_local_id, name="biosampleInCollection__collection_local_id", curie=EX.curie('collection_local_id'),
                   model_uri=EX.biosampleInCollection__collection_local_id, domain=None, range=str)

slots.subjectInCollection__subject_id_namespace = Slot(uri=EX.subject_id_namespace, name="subjectInCollection__subject_id_namespace", curie=EX.curie('subject_id_namespace'),
                   model_uri=EX.subjectInCollection__subject_id_namespace, domain=None, range=str)

slots.subjectInCollection__subject_local_id = Slot(uri=EX.subject_local_id, name="subjectInCollection__subject_local_id", curie=EX.curie('subject_local_id'),
                   model_uri=EX.subjectInCollection__subject_local_id, domain=None, range=str)

slots.subjectInCollection__collection_id_namespace = Slot(uri=EX.collection_id_namespace, name="subjectInCollection__collection_id_namespace", curie=EX.curie('collection_id_namespace'),
                   model_uri=EX.subjectInCollection__collection_id_namespace, domain=None, range=str)

slots.subjectInCollection__collection_local_id = Slot(uri=EX.collection_local_id, name="subjectInCollection__collection_local_id", curie=EX.curie('collection_local_id'),
                   model_uri=EX.subjectInCollection__collection_local_id, domain=None, range=str)

slots.fileDescribesBiosample__file_id_namespace = Slot(uri=EX.file_id_namespace, name="fileDescribesBiosample__file_id_namespace", curie=EX.curie('file_id_namespace'),
                   model_uri=EX.fileDescribesBiosample__file_id_namespace, domain=None, range=str)

slots.fileDescribesBiosample__file_local_id = Slot(uri=EX.file_local_id, name="fileDescribesBiosample__file_local_id", curie=EX.curie('file_local_id'),
                   model_uri=EX.fileDescribesBiosample__file_local_id, domain=None, range=str)

slots.fileDescribesBiosample__biosample_id_namespace = Slot(uri=EX.biosample_id_namespace, name="fileDescribesBiosample__biosample_id_namespace", curie=EX.curie('biosample_id_namespace'),
                   model_uri=EX.fileDescribesBiosample__biosample_id_namespace, domain=None, range=str)

slots.fileDescribesBiosample__biosample_local_id = Slot(uri=EX.biosample_local_id, name="fileDescribesBiosample__biosample_local_id", curie=EX.curie('biosample_local_id'),
                   model_uri=EX.fileDescribesBiosample__biosample_local_id, domain=None, range=str)

slots.fileDescribesSubject__file_id_namespace = Slot(uri=EX.file_id_namespace, name="fileDescribesSubject__file_id_namespace", curie=EX.curie('file_id_namespace'),
                   model_uri=EX.fileDescribesSubject__file_id_namespace, domain=None, range=str)

slots.fileDescribesSubject__file_local_id = Slot(uri=EX.file_local_id, name="fileDescribesSubject__file_local_id", curie=EX.curie('file_local_id'),
                   model_uri=EX.fileDescribesSubject__file_local_id, domain=None, range=str)

slots.fileDescribesSubject__subject_id_namespace = Slot(uri=EX.subject_id_namespace, name="fileDescribesSubject__subject_id_namespace", curie=EX.curie('subject_id_namespace'),
                   model_uri=EX.fileDescribesSubject__subject_id_namespace, domain=None, range=str)

slots.fileDescribesSubject__subject_local_id = Slot(uri=EX.subject_local_id, name="fileDescribesSubject__subject_local_id", curie=EX.curie('subject_local_id'),
                   model_uri=EX.fileDescribesSubject__subject_local_id, domain=None, range=str)

slots.biosampleFromSubject__biosample_id_namespace = Slot(uri=EX.biosample_id_namespace, name="biosampleFromSubject__biosample_id_namespace", curie=EX.curie('biosample_id_namespace'),
                   model_uri=EX.biosampleFromSubject__biosample_id_namespace, domain=None, range=str)

slots.biosampleFromSubject__biosample_local_id = Slot(uri=EX.biosample_local_id, name="biosampleFromSubject__biosample_local_id", curie=EX.curie('biosample_local_id'),
                   model_uri=EX.biosampleFromSubject__biosample_local_id, domain=None, range=str)

slots.biosampleFromSubject__subject_id_namespace = Slot(uri=EX.subject_id_namespace, name="biosampleFromSubject__subject_id_namespace", curie=EX.curie('subject_id_namespace'),
                   model_uri=EX.biosampleFromSubject__subject_id_namespace, domain=None, range=str)

slots.biosampleFromSubject__subject_local_id = Slot(uri=EX.subject_local_id, name="biosampleFromSubject__subject_local_id", curie=EX.curie('subject_local_id'),
                   model_uri=EX.biosampleFromSubject__subject_local_id, domain=None, range=str)

slots.biosampleFromSubject__age_at_sampling = Slot(uri=EX.age_at_sampling, name="biosampleFromSubject__age_at_sampling", curie=EX.curie('age_at_sampling'),
                   model_uri=EX.biosampleFromSubject__age_at_sampling, domain=None, range=Optional[Decimal])

slots.biosampleDisease__biosample_id_namespace = Slot(uri=EX.biosample_id_namespace, name="biosampleDisease__biosample_id_namespace", curie=EX.curie('biosample_id_namespace'),
                   model_uri=EX.biosampleDisease__biosample_id_namespace, domain=None, range=str)

slots.biosampleDisease__biosample_local_id = Slot(uri=EX.biosample_local_id, name="biosampleDisease__biosample_local_id", curie=EX.curie('biosample_local_id'),
                   model_uri=EX.biosampleDisease__biosample_local_id, domain=None, range=str)

slots.biosampleDisease__association_type = Slot(uri=EX.association_type, name="biosampleDisease__association_type", curie=EX.curie('association_type'),
                   model_uri=EX.biosampleDisease__association_type, domain=None, range=Union[str, "AssociationTypeEnum"])

slots.biosampleDisease__disease = Slot(uri=EX.disease, name="biosampleDisease__disease", curie=EX.curie('disease'),
                   model_uri=EX.biosampleDisease__disease, domain=None, range=str)

slots.subjectDisease__subject_id_namespace = Slot(uri=EX.subject_id_namespace, name="subjectDisease__subject_id_namespace", curie=EX.curie('subject_id_namespace'),
                   model_uri=EX.subjectDisease__subject_id_namespace, domain=None, range=str)

slots.subjectDisease__subject_local_id = Slot(uri=EX.subject_local_id, name="subjectDisease__subject_local_id", curie=EX.curie('subject_local_id'),
                   model_uri=EX.subjectDisease__subject_local_id, domain=None, range=str)

slots.subjectDisease__association_type = Slot(uri=EX.association_type, name="subjectDisease__association_type", curie=EX.curie('association_type'),
                   model_uri=EX.subjectDisease__association_type, domain=None, range=Union[str, "AssociationTypeEnum"])

slots.subjectDisease__disease = Slot(uri=EX.disease, name="subjectDisease__disease", curie=EX.curie('disease'),
                   model_uri=EX.subjectDisease__disease, domain=None, range=str)

slots.collectionDisease__collection_id_namespace = Slot(uri=EX.collection_id_namespace, name="collectionDisease__collection_id_namespace", curie=EX.curie('collection_id_namespace'),
                   model_uri=EX.collectionDisease__collection_id_namespace, domain=None, range=str)

slots.collectionDisease__collection_local_id = Slot(uri=EX.collection_local_id, name="collectionDisease__collection_local_id", curie=EX.curie('collection_local_id'),
                   model_uri=EX.collectionDisease__collection_local_id, domain=None, range=str)

slots.collectionDisease__disease = Slot(uri=EX.disease, name="collectionDisease__disease", curie=EX.curie('disease'),
                   model_uri=EX.collectionDisease__disease, domain=None, range=str)

slots.collectionPhenotype__collection_id_namespace = Slot(uri=EX.collection_id_namespace, name="collectionPhenotype__collection_id_namespace", curie=EX.curie('collection_id_namespace'),
                   model_uri=EX.collectionPhenotype__collection_id_namespace, domain=None, range=str)

slots.collectionPhenotype__collection_local_id = Slot(uri=EX.collection_local_id, name="collectionPhenotype__collection_local_id", curie=EX.curie('collection_local_id'),
                   model_uri=EX.collectionPhenotype__collection_local_id, domain=None, range=str)

slots.collectionPhenotype__phenotype = Slot(uri=EX.phenotype, name="collectionPhenotype__phenotype", curie=EX.curie('phenotype'),
                   model_uri=EX.collectionPhenotype__phenotype, domain=None, range=str)

slots.collectionGene__collection_id_namespace = Slot(uri=EX.collection_id_namespace, name="collectionGene__collection_id_namespace", curie=EX.curie('collection_id_namespace'),
                   model_uri=EX.collectionGene__collection_id_namespace, domain=None, range=str)

slots.collectionGene__collection_local_id = Slot(uri=EX.collection_local_id, name="collectionGene__collection_local_id", curie=EX.curie('collection_local_id'),
                   model_uri=EX.collectionGene__collection_local_id, domain=None, range=str)

slots.collectionGene__gene = Slot(uri=EX.gene, name="collectionGene__gene", curie=EX.curie('gene'),
                   model_uri=EX.collectionGene__gene, domain=None, range=str)

slots.collectionCompound__collection_id_namespace = Slot(uri=EX.collection_id_namespace, name="collectionCompound__collection_id_namespace", curie=EX.curie('collection_id_namespace'),
                   model_uri=EX.collectionCompound__collection_id_namespace, domain=None, range=str)

slots.collectionCompound__collection_local_id = Slot(uri=EX.collection_local_id, name="collectionCompound__collection_local_id", curie=EX.curie('collection_local_id'),
                   model_uri=EX.collectionCompound__collection_local_id, domain=None, range=str)

slots.collectionCompound__compound = Slot(uri=EX.compound, name="collectionCompound__compound", curie=EX.curie('compound'),
                   model_uri=EX.collectionCompound__compound, domain=None, range=str)

slots.collectionSubstance__collection_id_namespace = Slot(uri=EX.collection_id_namespace, name="collectionSubstance__collection_id_namespace", curie=EX.curie('collection_id_namespace'),
                   model_uri=EX.collectionSubstance__collection_id_namespace, domain=None, range=str)

slots.collectionSubstance__collection_local_id = Slot(uri=EX.collection_local_id, name="collectionSubstance__collection_local_id", curie=EX.curie('collection_local_id'),
                   model_uri=EX.collectionSubstance__collection_local_id, domain=None, range=str)

slots.collectionSubstance__substance = Slot(uri=EX.substance, name="collectionSubstance__substance", curie=EX.curie('substance'),
                   model_uri=EX.collectionSubstance__substance, domain=None, range=str)

slots.collectionTaxonomy__collection_id_namespace = Slot(uri=EX.collection_id_namespace, name="collectionTaxonomy__collection_id_namespace", curie=EX.curie('collection_id_namespace'),
                   model_uri=EX.collectionTaxonomy__collection_id_namespace, domain=None, range=str)

slots.collectionTaxonomy__collection_local_id = Slot(uri=EX.collection_local_id, name="collectionTaxonomy__collection_local_id", curie=EX.curie('collection_local_id'),
                   model_uri=EX.collectionTaxonomy__collection_local_id, domain=None, range=str)

slots.collectionTaxonomy__taxon = Slot(uri=EX.taxon, name="collectionTaxonomy__taxon", curie=EX.curie('taxon'),
                   model_uri=EX.collectionTaxonomy__taxon, domain=None, range=str)

slots.collectionAnatomy__collection_id_namespace = Slot(uri=EX.collection_id_namespace, name="collectionAnatomy__collection_id_namespace", curie=EX.curie('collection_id_namespace'),
                   model_uri=EX.collectionAnatomy__collection_id_namespace, domain=None, range=str)

slots.collectionAnatomy__collection_local_id = Slot(uri=EX.collection_local_id, name="collectionAnatomy__collection_local_id", curie=EX.curie('collection_local_id'),
                   model_uri=EX.collectionAnatomy__collection_local_id, domain=None, range=str)

slots.collectionAnatomy__anatomy = Slot(uri=EX.anatomy, name="collectionAnatomy__anatomy", curie=EX.curie('anatomy'),
                   model_uri=EX.collectionAnatomy__anatomy, domain=None, range=str)

slots.collectionProtein__collection_id_namespace = Slot(uri=EX.collection_id_namespace, name="collectionProtein__collection_id_namespace", curie=EX.curie('collection_id_namespace'),
                   model_uri=EX.collectionProtein__collection_id_namespace, domain=None, range=str)

slots.collectionProtein__collection_local_id = Slot(uri=EX.collection_local_id, name="collectionProtein__collection_local_id", curie=EX.curie('collection_local_id'),
                   model_uri=EX.collectionProtein__collection_local_id, domain=None, range=str)

slots.collectionProtein__protein = Slot(uri=EX.protein, name="collectionProtein__protein", curie=EX.curie('protein'),
                   model_uri=EX.collectionProtein__protein, domain=None, range=str)

slots.subjectPhenotype__subject_id_namespace = Slot(uri=EX.subject_id_namespace, name="subjectPhenotype__subject_id_namespace", curie=EX.curie('subject_id_namespace'),
                   model_uri=EX.subjectPhenotype__subject_id_namespace, domain=None, range=str)

slots.subjectPhenotype__subject_local_id = Slot(uri=EX.subject_local_id, name="subjectPhenotype__subject_local_id", curie=EX.curie('subject_local_id'),
                   model_uri=EX.subjectPhenotype__subject_local_id, domain=None, range=str)

slots.subjectPhenotype__association_type = Slot(uri=EX.association_type, name="subjectPhenotype__association_type", curie=EX.curie('association_type'),
                   model_uri=EX.subjectPhenotype__association_type, domain=None, range=Union[str, "AssociationTypeEnum"])

slots.subjectPhenotype__phenotype = Slot(uri=EX.phenotype, name="subjectPhenotype__phenotype", curie=EX.curie('phenotype'),
                   model_uri=EX.subjectPhenotype__phenotype, domain=None, range=str)

slots.biosampleSubstance__biosample_id_namespace = Slot(uri=EX.biosample_id_namespace, name="biosampleSubstance__biosample_id_namespace", curie=EX.curie('biosample_id_namespace'),
                   model_uri=EX.biosampleSubstance__biosample_id_namespace, domain=None, range=str)

slots.biosampleSubstance__biosample_local_id = Slot(uri=EX.biosample_local_id, name="biosampleSubstance__biosample_local_id", curie=EX.curie('biosample_local_id'),
                   model_uri=EX.biosampleSubstance__biosample_local_id, domain=None, range=str)

slots.biosampleSubstance__substance = Slot(uri=EX.substance, name="biosampleSubstance__substance", curie=EX.curie('substance'),
                   model_uri=EX.biosampleSubstance__substance, domain=None, range=str)

slots.subjectSubstance__subject_id_namespace = Slot(uri=EX.subject_id_namespace, name="subjectSubstance__subject_id_namespace", curie=EX.curie('subject_id_namespace'),
                   model_uri=EX.subjectSubstance__subject_id_namespace, domain=None, range=str)

slots.subjectSubstance__subject_local_id = Slot(uri=EX.subject_local_id, name="subjectSubstance__subject_local_id", curie=EX.curie('subject_local_id'),
                   model_uri=EX.subjectSubstance__subject_local_id, domain=None, range=str)

slots.subjectSubstance__substance = Slot(uri=EX.substance, name="subjectSubstance__substance", curie=EX.curie('substance'),
                   model_uri=EX.subjectSubstance__substance, domain=None, range=str)

slots.biosampleGene__biosample_id_namespace = Slot(uri=EX.biosample_id_namespace, name="biosampleGene__biosample_id_namespace", curie=EX.curie('biosample_id_namespace'),
                   model_uri=EX.biosampleGene__biosample_id_namespace, domain=None, range=str)

slots.biosampleGene__biosample_local_id = Slot(uri=EX.biosample_local_id, name="biosampleGene__biosample_local_id", curie=EX.curie('biosample_local_id'),
                   model_uri=EX.biosampleGene__biosample_local_id, domain=None, range=str)

slots.biosampleGene__gene = Slot(uri=EX.gene, name="biosampleGene__gene", curie=EX.curie('gene'),
                   model_uri=EX.biosampleGene__gene, domain=None, range=str)

slots.phenotypeGene__phenotype = Slot(uri=EX.phenotype, name="phenotypeGene__phenotype", curie=EX.curie('phenotype'),
                   model_uri=EX.phenotypeGene__phenotype, domain=None, range=str)

slots.phenotypeGene__gene = Slot(uri=EX.gene, name="phenotypeGene__gene", curie=EX.curie('gene'),
                   model_uri=EX.phenotypeGene__gene, domain=None, range=str)

slots.phenotypeDisease__phenotype = Slot(uri=EX.phenotype, name="phenotypeDisease__phenotype", curie=EX.curie('phenotype'),
                   model_uri=EX.phenotypeDisease__phenotype, domain=None, range=str)

slots.phenotypeDisease__disease = Slot(uri=EX.disease, name="phenotypeDisease__disease", curie=EX.curie('disease'),
                   model_uri=EX.phenotypeDisease__disease, domain=None, range=str)

slots.subjectRace__subject_id_namespace = Slot(uri=EX.subject_id_namespace, name="subjectRace__subject_id_namespace", curie=EX.curie('subject_id_namespace'),
                   model_uri=EX.subjectRace__subject_id_namespace, domain=None, range=str)

slots.subjectRace__subject_local_id = Slot(uri=EX.subject_local_id, name="subjectRace__subject_local_id", curie=EX.curie('subject_local_id'),
                   model_uri=EX.subjectRace__subject_local_id, domain=None, range=str)

slots.subjectRace__race = Slot(uri=EX.race, name="subjectRace__race", curie=EX.curie('race'),
                   model_uri=EX.subjectRace__race, domain=None, range=Optional[Union[str, "RaceEnum"]])

slots.subjectRoleTaxonomy__subject_id_namespace = Slot(uri=EX.subject_id_namespace, name="subjectRoleTaxonomy__subject_id_namespace", curie=EX.curie('subject_id_namespace'),
                   model_uri=EX.subjectRoleTaxonomy__subject_id_namespace, domain=None, range=str)

slots.subjectRoleTaxonomy__subject_local_id = Slot(uri=EX.subject_local_id, name="subjectRoleTaxonomy__subject_local_id", curie=EX.curie('subject_local_id'),
                   model_uri=EX.subjectRoleTaxonomy__subject_local_id, domain=None, range=str)

slots.subjectRoleTaxonomy__role_id = Slot(uri=EX.role_id, name="subjectRoleTaxonomy__role_id", curie=EX.curie('role_id'),
                   model_uri=EX.subjectRoleTaxonomy__role_id, domain=None, range=Union[str, "RoleIdEnum"])

slots.subjectRoleTaxonomy__taxonomy_id = Slot(uri=EX.taxonomy_id, name="subjectRoleTaxonomy__taxonomy_id", curie=EX.curie('taxonomy_id'),
                   model_uri=EX.subjectRoleTaxonomy__taxonomy_id, domain=None, range=str)

slots.assayType__id = Slot(uri=EX.id, name="assayType__id", curie=EX.curie('id'),
                   model_uri=EX.assayType__id, domain=None, range=str)

slots.assayType__description = Slot(uri=EX.description, name="assayType__description", curie=EX.curie('description'),
                   model_uri=EX.assayType__description, domain=None, range=Optional[str])

slots.assayType__synonyms = Slot(uri=EX.synonyms, name="assayType__synonyms", curie=EX.curie('synonyms'),
                   model_uri=EX.assayType__synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.analysisType__id = Slot(uri=EX.id, name="analysisType__id", curie=EX.curie('id'),
                   model_uri=EX.analysisType__id, domain=None, range=str)

slots.analysisType__description = Slot(uri=EX.description, name="analysisType__description", curie=EX.curie('description'),
                   model_uri=EX.analysisType__description, domain=None, range=Optional[str])

slots.analysisType__synonyms = Slot(uri=EX.synonyms, name="analysisType__synonyms", curie=EX.curie('synonyms'),
                   model_uri=EX.analysisType__synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.ncbiTaxonomy__id = Slot(uri=EX.id, name="ncbiTaxonomy__id", curie=EX.curie('id'),
                   model_uri=EX.ncbiTaxonomy__id, domain=None, range=str,
                   pattern=re.compile(r'^NCBI:txid[0-9]+$'))

slots.ncbiTaxonomy__clade = Slot(uri=EX.clade, name="ncbiTaxonomy__clade", curie=EX.curie('clade'),
                   model_uri=EX.ncbiTaxonomy__clade, domain=None, range=str)

slots.ncbiTaxonomy__description = Slot(uri=EX.description, name="ncbiTaxonomy__description", curie=EX.curie('description'),
                   model_uri=EX.ncbiTaxonomy__description, domain=None, range=Optional[str])

slots.ncbiTaxonomy__synonyms = Slot(uri=EX.synonyms, name="ncbiTaxonomy__synonyms", curie=EX.curie('synonyms'),
                   model_uri=EX.ncbiTaxonomy__synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.anatomy__id = Slot(uri=EX.id, name="anatomy__id", curie=EX.curie('id'),
                   model_uri=EX.anatomy__id, domain=None, range=str)

slots.anatomy__description = Slot(uri=EX.description, name="anatomy__description", curie=EX.curie('description'),
                   model_uri=EX.anatomy__description, domain=None, range=Optional[str])

slots.anatomy__synonyms = Slot(uri=EX.synonyms, name="anatomy__synonyms", curie=EX.curie('synonyms'),
                   model_uri=EX.anatomy__synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.fileFormat__id = Slot(uri=EX.id, name="fileFormat__id", curie=EX.curie('id'),
                   model_uri=EX.fileFormat__id, domain=None, range=str)

slots.fileFormat__description = Slot(uri=EX.description, name="fileFormat__description", curie=EX.curie('description'),
                   model_uri=EX.fileFormat__description, domain=None, range=Optional[str])

slots.fileFormat__synonyms = Slot(uri=EX.synonyms, name="fileFormat__synonyms", curie=EX.curie('synonyms'),
                   model_uri=EX.fileFormat__synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.dataType__id = Slot(uri=EX.id, name="dataType__id", curie=EX.curie('id'),
                   model_uri=EX.dataType__id, domain=None, range=str)

slots.dataType__description = Slot(uri=EX.description, name="dataType__description", curie=EX.curie('description'),
                   model_uri=EX.dataType__description, domain=None, range=Optional[str])

slots.dataType__synonyms = Slot(uri=EX.synonyms, name="dataType__synonyms", curie=EX.curie('synonyms'),
                   model_uri=EX.dataType__synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.disease__id = Slot(uri=EX.id, name="disease__id", curie=EX.curie('id'),
                   model_uri=EX.disease__id, domain=None, range=str)

slots.disease__description = Slot(uri=EX.description, name="disease__description", curie=EX.curie('description'),
                   model_uri=EX.disease__description, domain=None, range=Optional[str])

slots.disease__synonyms = Slot(uri=EX.synonyms, name="disease__synonyms", curie=EX.curie('synonyms'),
                   model_uri=EX.disease__synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.phenotype__id = Slot(uri=EX.id, name="phenotype__id", curie=EX.curie('id'),
                   model_uri=EX.phenotype__id, domain=None, range=str)

slots.phenotype__description = Slot(uri=EX.description, name="phenotype__description", curie=EX.curie('description'),
                   model_uri=EX.phenotype__description, domain=None, range=Optional[str])

slots.phenotype__synonyms = Slot(uri=EX.synonyms, name="phenotype__synonyms", curie=EX.curie('synonyms'),
                   model_uri=EX.phenotype__synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.compound__id = Slot(uri=EX.id, name="compound__id", curie=EX.curie('id'),
                   model_uri=EX.compound__id, domain=None, range=str)

slots.compound__description = Slot(uri=EX.description, name="compound__description", curie=EX.curie('description'),
                   model_uri=EX.compound__description, domain=None, range=Optional[str])

slots.compound__synonyms = Slot(uri=EX.synonyms, name="compound__synonyms", curie=EX.curie('synonyms'),
                   model_uri=EX.compound__synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.substance__id = Slot(uri=EX.id, name="substance__id", curie=EX.curie('id'),
                   model_uri=EX.substance__id, domain=None, range=str)

slots.substance__description = Slot(uri=EX.description, name="substance__description", curie=EX.curie('description'),
                   model_uri=EX.substance__description, domain=None, range=Optional[str])

slots.substance__synonyms = Slot(uri=EX.synonyms, name="substance__synonyms", curie=EX.curie('synonyms'),
                   model_uri=EX.substance__synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.substance__compound = Slot(uri=EX.compound, name="substance__compound", curie=EX.curie('compound'),
                   model_uri=EX.substance__compound, domain=None, range=str)

slots.gene__id = Slot(uri=EX.id, name="gene__id", curie=EX.curie('id'),
                   model_uri=EX.gene__id, domain=None, range=str)

slots.gene__description = Slot(uri=EX.description, name="gene__description", curie=EX.curie('description'),
                   model_uri=EX.gene__description, domain=None, range=Optional[str])

slots.gene__synonyms = Slot(uri=EX.synonyms, name="gene__synonyms", curie=EX.curie('synonyms'),
                   model_uri=EX.gene__synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.gene__organism = Slot(uri=EX.organism, name="gene__organism", curie=EX.curie('organism'),
                   model_uri=EX.gene__organism, domain=None, range=str,
                   pattern=re.compile(r'^NCBI:txid[0-9]+$'))

slots.protein__id = Slot(uri=EX.id, name="protein__id", curie=EX.curie('id'),
                   model_uri=EX.protein__id, domain=None, range=str)

slots.protein__description = Slot(uri=EX.description, name="protein__description", curie=EX.curie('description'),
                   model_uri=EX.protein__description, domain=None, range=Optional[str])

slots.protein__synonyms = Slot(uri=EX.synonyms, name="protein__synonyms", curie=EX.curie('synonyms'),
                   model_uri=EX.protein__synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.protein__organism = Slot(uri=EX.organism, name="protein__organism", curie=EX.curie('organism'),
                   model_uri=EX.protein__organism, domain=None, range=Optional[str],
                   pattern=re.compile(r'^NCBI:txid[0-9]+$'))

slots.proteinGene__protein = Slot(uri=EX.protein, name="proteinGene__protein", curie=EX.curie('protein'),
                   model_uri=EX.proteinGene__protein, domain=None, range=str)

slots.proteinGene__gene = Slot(uri=EX.gene, name="proteinGene__gene", curie=EX.curie('gene'),
                   model_uri=EX.proteinGene__gene, domain=None, range=str)

slots.idNamespace__id = Slot(uri=EX.id, name="idNamespace__id", curie=EX.curie('id'),
                   model_uri=EX.idNamespace__id, domain=None, range=str)

slots.idNamespace__abbreviation = Slot(uri=EX.abbreviation, name="idNamespace__abbreviation", curie=EX.curie('abbreviation'),
                   model_uri=EX.idNamespace__abbreviation, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-zA-Z0-9_]+$'))

slots.idNamespace__description = Slot(uri=EX.description, name="idNamespace__description", curie=EX.curie('description'),
                   model_uri=EX.idNamespace__description, domain=None, range=Optional[str])