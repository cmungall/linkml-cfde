# Auto generated from cfde.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-07-08T14:49:22
# Schema: cfde_schema
#
# id: https://w3id.org/linkml/cfde
# description: A complete list of schematic specifications for the resources (TSV table files) that will be used
#              to represent C2M2 DCC metadata prior to ingest into the C2M2 database system
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
CFDE_DISEASE_ASSOCIATION_TYPE = CurieNamespace('cfde_disease_association_type', 'https://w3id.org/linkml/cfde/cfde_disease_association_type/')
CFDE_PHENOTYPE_ASSOCIATION_TYPE = CurieNamespace('cfde_phenotype_association_type', 'https://w3id.org/linkml/cfde/cfde_phenotype_association_type/')
CFDE_SCHEMA = CurieNamespace('cfde_schema', 'https://w3id.org/linkml/cfde/')
CFDE_SUBJECT_ETHNICITY = CurieNamespace('cfde_subject_ethnicity', 'https://w3id.org/linkml/cfde/cfde_subject_ethnicity/')
CFDE_SUBJECT_GRANULARITY = CurieNamespace('cfde_subject_granularity', 'https://w3id.org/linkml/cfde/cfde_subject_granularity/')
CFDE_SUBJECT_RACE = CurieNamespace('cfde_subject_race', 'https://w3id.org/linkml/cfde/cfde_subject_race/')
CFDE_SUBJECT_ROLE = CurieNamespace('cfde_subject_role', 'https://w3id.org/linkml/cfde/cfde_subject_role/')
CFDE_SUBJECT_SEX = CurieNamespace('cfde_subject_sex', 'https://w3id.org/linkml/cfde/cfde_subject_sex/')
EX = CurieNamespace('ex', 'https://example.org/test/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = CFDE_SCHEMA


# Types

# Class references
class DccId(extended_str):
    pass


class AssayTypeId(extended_str):
    pass


class AnalysisTypeId(extended_str):
    pass


class NcbiTaxonomyId(extended_str):
    pass


class AnatomyId(extended_str):
    pass


class FileFormatId(extended_str):
    pass


class DataTypeId(extended_str):
    pass


class DiseaseId(extended_str):
    pass


class PhenotypeId(extended_str):
    pass


class CompoundId(extended_str):
    pass


class SubstanceId(extended_str):
    pass


class GeneId(extended_str):
    pass


class ProteinId(extended_str):
    pass


class IdNamespaceId(extended_str):
    pass


@dataclass
class File(YAMLRoot):
    """
    A stable digital asset
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.File
    class_class_curie: ClassVar[str] = "cfde_schema:File"
    class_name: ClassVar[str] = "file"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.File

    id_namespace: Union[str, IdNamespaceId] = None
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
    file_format: Optional[Union[str, FileFormatId]] = None
    compression_format: Optional[Union[str, FileFormatId]] = None
    data_type: Optional[Union[str, DataTypeId]] = None
    assay_type: Optional[Union[str, AssayTypeId]] = None
    analysis_type: Optional[Union[str, AnalysisTypeId]] = None
    mime_type: Optional[str] = None
    bundle_collection_id_namespace: Optional[str] = None
    bundle_collection_local_id: Optional[str] = None
    dbgap_study_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id_namespace):
            self.MissingRequiredField("id_namespace")
        if not isinstance(self.id_namespace, IdNamespaceId):
            self.id_namespace = IdNamespaceId(self.id_namespace)

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

        if self.file_format is not None and not isinstance(self.file_format, FileFormatId):
            self.file_format = FileFormatId(self.file_format)

        if self.compression_format is not None and not isinstance(self.compression_format, FileFormatId):
            self.compression_format = FileFormatId(self.compression_format)

        if self.data_type is not None and not isinstance(self.data_type, DataTypeId):
            self.data_type = DataTypeId(self.data_type)

        if self.assay_type is not None and not isinstance(self.assay_type, AssayTypeId):
            self.assay_type = AssayTypeId(self.assay_type)

        if self.analysis_type is not None and not isinstance(self.analysis_type, AnalysisTypeId):
            self.analysis_type = AnalysisTypeId(self.analysis_type)

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
    A tissue sample or other physical specimen
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.Biosample
    class_class_curie: ClassVar[str] = "cfde_schema:Biosample"
    class_name: ClassVar[str] = "biosample"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.Biosample

    id_namespace: Union[str, IdNamespaceId] = None
    local_id: str = None
    project_id_namespace: str = None
    project_local_id: str = None
    persistent_id: Optional[str] = None
    creation_time: Optional[Union[str, XSDDateTime]] = None
    assay_type: Optional[Union[str, AssayTypeId]] = None
    anatomy: Optional[Union[str, AnatomyId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id_namespace):
            self.MissingRequiredField("id_namespace")
        if not isinstance(self.id_namespace, IdNamespaceId):
            self.id_namespace = IdNamespaceId(self.id_namespace)

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

        if self.assay_type is not None and not isinstance(self.assay_type, AssayTypeId):
            self.assay_type = AssayTypeId(self.assay_type)

        if self.anatomy is not None and not isinstance(self.anatomy, AnatomyId):
            self.anatomy = AnatomyId(self.anatomy)

        super().__post_init__(**kwargs)


@dataclass
class Subject(YAMLRoot):
    """
    A biological entity from which a C2M2 biosample can in principle be generated
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.Subject
    class_class_curie: ClassVar[str] = "cfde_schema:Subject"
    class_name: ClassVar[str] = "subject"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.Subject

    id_namespace: Union[str, IdNamespaceId] = None
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
        if not isinstance(self.id_namespace, IdNamespaceId):
            self.id_namespace = IdNamespaceId(self.id_namespace)

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
    The Common Fund program or data coordinating center (DCC, identified by the given project foreign key) that
    produced this C2M2 instance
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.Dcc
    class_class_curie: ClassVar[str] = "cfde_schema:Dcc"
    class_name: ClassVar[str] = "dcc"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.Dcc

    id: Union[str, DccId] = None
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
        if not isinstance(self.id, DccId):
            self.id = DccId(self.id)

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
    A node in the C2M2 project hierarchy subdividing all resources described by this DCC's C2M2 metadata
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.Project
    class_class_curie: ClassVar[str] = "cfde_schema:Project"
    class_name: ClassVar[str] = "project"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.Project

    id_namespace: Union[str, IdNamespaceId] = None
    local_id: str = None
    persistent_id: Optional[str] = None
    creation_time: Optional[Union[str, XSDDateTime]] = None
    abbreviation: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id_namespace):
            self.MissingRequiredField("id_namespace")
        if not isinstance(self.id_namespace, IdNamespaceId):
            self.id_namespace = IdNamespaceId(self.id_namespace)

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
    Association between a child project and its parent
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.ProjectInProject
    class_class_curie: ClassVar[str] = "cfde_schema:ProjectInProject"
    class_name: ClassVar[str] = "project_in_project"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.ProjectInProject

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
    A grouping of C2M2 files, biosamples and/or subjects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.Collection
    class_class_curie: ClassVar[str] = "cfde_schema:Collection"
    class_name: ClassVar[str] = "collection"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.Collection

    id_namespace: Union[str, IdNamespaceId] = None
    local_id: str = None
    persistent_id: Optional[str] = None
    creation_time: Optional[Union[str, XSDDateTime]] = None
    abbreviation: Optional[str] = None
    description: Optional[str] = None
    has_time_series_data: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id_namespace):
            self.MissingRequiredField("id_namespace")
        if not isinstance(self.id_namespace, IdNamespaceId):
            self.id_namespace = IdNamespaceId(self.id_namespace)

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
    Association between a containing collection (superset) and a contained collection (subset)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.CollectionInCollection
    class_class_curie: ClassVar[str] = "cfde_schema:CollectionInCollection"
    class_name: ClassVar[str] = "collection_in_collection"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.CollectionInCollection

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
    Association between a summary file and an entire collection described by that file
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.FileDescribesCollection
    class_class_curie: ClassVar[str] = "cfde_schema:FileDescribesCollection"
    class_name: ClassVar[str] = "file_describes_collection"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.FileDescribesCollection

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
    (Shallow) association between a collection and a project that defined it
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.CollectionDefinedByProject
    class_class_curie: ClassVar[str] = "cfde_schema:CollectionDefinedByProject"
    class_name: ClassVar[str] = "collection_defined_by_project"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.CollectionDefinedByProject

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
    Association between a file and a (containing) collection
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.FileInCollection
    class_class_curie: ClassVar[str] = "cfde_schema:FileInCollection"
    class_name: ClassVar[str] = "file_in_collection"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.FileInCollection

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
    Association between a biosample and a (containing) collection
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.BiosampleInCollection
    class_class_curie: ClassVar[str] = "cfde_schema:BiosampleInCollection"
    class_name: ClassVar[str] = "biosample_in_collection"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.BiosampleInCollection

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
    Association between a subject and a (containing) collection
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.SubjectInCollection
    class_class_curie: ClassVar[str] = "cfde_schema:SubjectInCollection"
    class_name: ClassVar[str] = "subject_in_collection"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.SubjectInCollection

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
    Association between a biosample and a file containing information about that biosample
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.FileDescribesBiosample
    class_class_curie: ClassVar[str] = "cfde_schema:FileDescribesBiosample"
    class_name: ClassVar[str] = "file_describes_biosample"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.FileDescribesBiosample

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
    Association between a subject and a file containing information about that subject
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.FileDescribesSubject
    class_class_curie: ClassVar[str] = "cfde_schema:FileDescribesSubject"
    class_name: ClassVar[str] = "file_describes_subject"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.FileDescribesSubject

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
    Association between a biosample and its source subject
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.BiosampleFromSubject
    class_class_curie: ClassVar[str] = "cfde_schema:BiosampleFromSubject"
    class_name: ClassVar[str] = "biosample_from_subject"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.BiosampleFromSubject

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
    Association between a C2M2 biosample and a disease positively (e.g. cancer tumor tissue sample) OR negatively
    (e.g. cancer-free tissue sample) identified for that biosample
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.BiosampleDisease
    class_class_curie: ClassVar[str] = "cfde_schema:BiosampleDisease"
    class_name: ClassVar[str] = "biosample_disease"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.BiosampleDisease

    biosample_id_namespace: str = None
    biosample_local_id: str = None
    association_type: Union[str, "AssociationTypeEnum"] = None
    disease: Union[str, DiseaseId] = None

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
        if not isinstance(self.disease, DiseaseId):
            self.disease = DiseaseId(self.disease)

        super().__post_init__(**kwargs)


@dataclass
class SubjectDisease(YAMLRoot):
    """
    Association between a C2M2 subject and a disease positively OR negatively clinically identified in that subject
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.SubjectDisease
    class_class_curie: ClassVar[str] = "cfde_schema:SubjectDisease"
    class_name: ClassVar[str] = "subject_disease"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.SubjectDisease

    subject_id_namespace: str = None
    subject_local_id: str = None
    association_type: Union[str, "AssociationTypeEnum"] = None
    disease: Union[str, DiseaseId] = None

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
        if not isinstance(self.disease, DiseaseId):
            self.disease = DiseaseId(self.disease)

        super().__post_init__(**kwargs)


@dataclass
class CollectionDisease(YAMLRoot):
    """
    Association between a disease and a C2M2 collection containing experimental resources directly related to the
    study of that disease
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.CollectionDisease
    class_class_curie: ClassVar[str] = "cfde_schema:CollectionDisease"
    class_name: ClassVar[str] = "collection_disease"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.CollectionDisease

    collection_id_namespace: str = None
    collection_local_id: str = None
    disease: Union[str, DiseaseId] = None

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
        if not isinstance(self.disease, DiseaseId):
            self.disease = DiseaseId(self.disease)

        super().__post_init__(**kwargs)


@dataclass
class CollectionPhenotype(YAMLRoot):
    """
    Association between a phenotype and a C2M2 collection containing experimental resources directly related to the
    study of that phenotype
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.CollectionPhenotype
    class_class_curie: ClassVar[str] = "cfde_schema:CollectionPhenotype"
    class_name: ClassVar[str] = "collection_phenotype"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.CollectionPhenotype

    collection_id_namespace: str = None
    collection_local_id: str = None
    phenotype: Union[str, PhenotypeId] = None

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
        if not isinstance(self.phenotype, PhenotypeId):
            self.phenotype = PhenotypeId(self.phenotype)

        super().__post_init__(**kwargs)


@dataclass
class CollectionGene(YAMLRoot):
    """
    Association between a gene and a C2M2 collection containing experimental resources directly related to the study
    of that gene
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.CollectionGene
    class_class_curie: ClassVar[str] = "cfde_schema:CollectionGene"
    class_name: ClassVar[str] = "collection_gene"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.CollectionGene

    collection_id_namespace: str = None
    collection_local_id: str = None
    gene: Union[str, GeneId] = None

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
        if not isinstance(self.gene, GeneId):
            self.gene = GeneId(self.gene)

        super().__post_init__(**kwargs)


@dataclass
class CollectionCompound(YAMLRoot):
    """
    Association between a compound and a C2M2 collection containing experimental resources directly related to the
    study of that compound
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.CollectionCompound
    class_class_curie: ClassVar[str] = "cfde_schema:CollectionCompound"
    class_name: ClassVar[str] = "collection_compound"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.CollectionCompound

    collection_id_namespace: str = None
    collection_local_id: str = None
    compound: Union[str, CompoundId] = None

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
        if not isinstance(self.compound, CompoundId):
            self.compound = CompoundId(self.compound)

        super().__post_init__(**kwargs)


@dataclass
class CollectionSubstance(YAMLRoot):
    """
    Association between a substance and a C2M2 collection containing experimental resources directly related to the
    study of that substance
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.CollectionSubstance
    class_class_curie: ClassVar[str] = "cfde_schema:CollectionSubstance"
    class_name: ClassVar[str] = "collection_substance"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.CollectionSubstance

    collection_id_namespace: str = None
    collection_local_id: str = None
    substance: Union[str, SubstanceId] = None

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
        if not isinstance(self.substance, SubstanceId):
            self.substance = SubstanceId(self.substance)

        super().__post_init__(**kwargs)


@dataclass
class CollectionTaxonomy(YAMLRoot):
    """
    Association between a taxon and a C2M2 collection containing experimental resources directly related to the study
    of that taxon
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.CollectionTaxonomy
    class_class_curie: ClassVar[str] = "cfde_schema:CollectionTaxonomy"
    class_name: ClassVar[str] = "collection_taxonomy"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.CollectionTaxonomy

    collection_id_namespace: str = None
    collection_local_id: str = None
    taxon: Union[str, NcbiTaxonomyId] = None

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
        if not isinstance(self.taxon, NcbiTaxonomyId):
            self.taxon = NcbiTaxonomyId(self.taxon)

        super().__post_init__(**kwargs)


@dataclass
class CollectionAnatomy(YAMLRoot):
    """
    Association between an UBERON anatomical term and a C2M2 collection containing experimental resources directly
    related to the study of the anatomical concept described by that term
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.CollectionAnatomy
    class_class_curie: ClassVar[str] = "cfde_schema:CollectionAnatomy"
    class_name: ClassVar[str] = "collection_anatomy"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.CollectionAnatomy

    collection_id_namespace: str = None
    collection_local_id: str = None
    anatomy: Union[str, AnatomyId] = None

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
        if not isinstance(self.anatomy, AnatomyId):
            self.anatomy = AnatomyId(self.anatomy)

        super().__post_init__(**kwargs)


@dataclass
class CollectionProtein(YAMLRoot):
    """
    Association between a protein and a C2M2 collection containing experimental resources directly related to the
    study of that protein
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.CollectionProtein
    class_class_curie: ClassVar[str] = "cfde_schema:CollectionProtein"
    class_name: ClassVar[str] = "collection_protein"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.CollectionProtein

    collection_id_namespace: str = None
    collection_local_id: str = None
    protein: Union[str, ProteinId] = None

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
        if not isinstance(self.protein, ProteinId):
            self.protein = ProteinId(self.protein)

        super().__post_init__(**kwargs)


@dataclass
class SubjectPhenotype(YAMLRoot):
    """
    Association between a C2M2 subject and a phenotype positively OR negatively clinically identified for that subject
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.SubjectPhenotype
    class_class_curie: ClassVar[str] = "cfde_schema:SubjectPhenotype"
    class_name: ClassVar[str] = "subject_phenotype"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.SubjectPhenotype

    subject_id_namespace: str = None
    subject_local_id: str = None
    association_type: Union[str, "AssociationTypeEnum"] = None
    phenotype: Union[str, PhenotypeId] = None

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
        if not isinstance(self.phenotype, PhenotypeId):
            self.phenotype = PhenotypeId(self.phenotype)

        super().__post_init__(**kwargs)


@dataclass
class BiosampleSubstance(YAMLRoot):
    """
    Association between a C2M2 biosample and a PubChem substance experimentally associated with that biosample
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.BiosampleSubstance
    class_class_curie: ClassVar[str] = "cfde_schema:BiosampleSubstance"
    class_name: ClassVar[str] = "biosample_substance"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.BiosampleSubstance

    biosample_id_namespace: str = None
    biosample_local_id: str = None
    substance: Union[str, SubstanceId] = None

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
        if not isinstance(self.substance, SubstanceId):
            self.substance = SubstanceId(self.substance)

        super().__post_init__(**kwargs)


@dataclass
class SubjectSubstance(YAMLRoot):
    """
    Association between a C2M2 subject and a PubChem substance experimentally associated with that subject
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.SubjectSubstance
    class_class_curie: ClassVar[str] = "cfde_schema:SubjectSubstance"
    class_name: ClassVar[str] = "subject_substance"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.SubjectSubstance

    subject_id_namespace: str = None
    subject_local_id: str = None
    substance: Union[str, SubstanceId] = None

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
        if not isinstance(self.substance, SubstanceId):
            self.substance = SubstanceId(self.substance)

        super().__post_init__(**kwargs)


@dataclass
class BiosampleGene(YAMLRoot):
    """
    Association between a C2M2 biosample and an Ensembl gene especially relevant to it
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.BiosampleGene
    class_class_curie: ClassVar[str] = "cfde_schema:BiosampleGene"
    class_name: ClassVar[str] = "biosample_gene"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.BiosampleGene

    biosample_id_namespace: str = None
    biosample_local_id: str = None
    gene: Union[str, GeneId] = None

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
        if not isinstance(self.gene, GeneId):
            self.gene = GeneId(self.gene)

        super().__post_init__(**kwargs)


@dataclass
class PhenotypeGene(YAMLRoot):
    """
    Association between a Human Phenotype Ontology term and an Ensembl gene especially relevant to it
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.PhenotypeGene
    class_class_curie: ClassVar[str] = "cfde_schema:PhenotypeGene"
    class_name: ClassVar[str] = "phenotype_gene"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.PhenotypeGene

    phenotype: Union[str, PhenotypeId] = None
    gene: Union[str, GeneId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.phenotype):
            self.MissingRequiredField("phenotype")
        if not isinstance(self.phenotype, PhenotypeId):
            self.phenotype = PhenotypeId(self.phenotype)

        if self._is_empty(self.gene):
            self.MissingRequiredField("gene")
        if not isinstance(self.gene, GeneId):
            self.gene = GeneId(self.gene)

        super().__post_init__(**kwargs)


@dataclass
class PhenotypeDisease(YAMLRoot):
    """
    Association between a Human Phenotype Ontology term and a Disease Ontology term identifying a disease especially
    relevant to it
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.PhenotypeDisease
    class_class_curie: ClassVar[str] = "cfde_schema:PhenotypeDisease"
    class_name: ClassVar[str] = "phenotype_disease"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.PhenotypeDisease

    phenotype: Union[str, PhenotypeId] = None
    disease: Union[str, DiseaseId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.phenotype):
            self.MissingRequiredField("phenotype")
        if not isinstance(self.phenotype, PhenotypeId):
            self.phenotype = PhenotypeId(self.phenotype)

        if self._is_empty(self.disease):
            self.MissingRequiredField("disease")
        if not isinstance(self.disease, DiseaseId):
            self.disease = DiseaseId(self.disease)

        super().__post_init__(**kwargs)


@dataclass
class SubjectRace(YAMLRoot):
    """
    Identification of a C2M2 subject with one or more self-selected races
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.SubjectRace
    class_class_curie: ClassVar[str] = "cfde_schema:SubjectRace"
    class_name: ClassVar[str] = "subject_race"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.SubjectRace

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
    Trinary association linking IDs representing (1) a subject, (2) a subject_role (a named organism-level constituent
    component of a subject, like 'host', 'pathogen', 'endosymbiont', 'taxon detected inside a microbiome subject',
    etc.) and (3) a taxonomic label (which is hereby assigned to this particular subject_role within this particular
    subject)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.SubjectRoleTaxonomy
    class_class_curie: ClassVar[str] = "cfde_schema:SubjectRoleTaxonomy"
    class_name: ClassVar[str] = "subject_role_taxonomy"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.SubjectRoleTaxonomy

    subject_id_namespace: str = None
    subject_local_id: str = None
    role_id: Union[str, "RoleIdEnum"] = None
    taxonomy_id: Union[str, NcbiTaxonomyId] = None

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
        if not isinstance(self.taxonomy_id, NcbiTaxonomyId):
            self.taxonomy_id = NcbiTaxonomyId(self.taxonomy_id)

        super().__post_init__(**kwargs)


@dataclass
class AssayType(YAMLRoot):
    """
    List of Ontology for Biomedical Investigations (OBI) CV terms used to describe types of experiment that generate
    C2M2 biosamples or results stored in C2M2 files
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.AssayType
    class_class_curie: ClassVar[str] = "cfde_schema:AssayType"
    class_name: ClassVar[str] = "assay_type"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.AssayType

    id: Union[str, AssayTypeId] = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssayTypeId):
            self.id = AssayTypeId(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        super().__post_init__(**kwargs)


@dataclass
class AnalysisType(YAMLRoot):
    """
    List of Ontology for Biomedical Investigations (OBI) CV terms used to describe analytic methods that generate C2M2
    files
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.AnalysisType
    class_class_curie: ClassVar[str] = "cfde_schema:AnalysisType"
    class_name: ClassVar[str] = "analysis_type"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.AnalysisType

    id: Union[str, AnalysisTypeId] = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnalysisTypeId):
            self.id = AnalysisTypeId(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        super().__post_init__(**kwargs)


@dataclass
class NcbiTaxonomy(YAMLRoot):
    """
    List of NCBI Taxonomy Database IDs identifying taxa used to describe C2M2 subjects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.NcbiTaxonomy
    class_class_curie: ClassVar[str] = "cfde_schema:NcbiTaxonomy"
    class_name: ClassVar[str] = "ncbi_taxonomy"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.NcbiTaxonomy

    id: Union[str, NcbiTaxonomyId] = None
    clade: str = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NcbiTaxonomyId):
            self.id = NcbiTaxonomyId(self.id)

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
    List of Uber-anatomy ontology (UBERON) CV terms used to locate the origin of a C2M2 biosample within the
    physiology of its source or host organism
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.Anatomy
    class_class_curie: ClassVar[str] = "cfde_schema:Anatomy"
    class_name: ClassVar[str] = "anatomy"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.Anatomy

    id: Union[str, AnatomyId] = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnatomyId):
            self.id = AnatomyId(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        super().__post_init__(**kwargs)


@dataclass
class FileFormat(YAMLRoot):
    """
    List of EDAM CV 'format:' terms used to describe formats of C2M2 files
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.FileFormat
    class_class_curie: ClassVar[str] = "cfde_schema:FileFormat"
    class_name: ClassVar[str] = "file_format"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.FileFormat

    id: Union[str, FileFormatId] = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FileFormatId):
            self.id = FileFormatId(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        super().__post_init__(**kwargs)


@dataclass
class DataType(YAMLRoot):
    """
    List of EDAM CV 'data:' terms used to describe data in C2M2 files
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.DataType
    class_class_curie: ClassVar[str] = "cfde_schema:DataType"
    class_name: ClassVar[str] = "data_type"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.DataType

    id: Union[str, DataTypeId] = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataTypeId):
            self.id = DataTypeId(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        super().__post_init__(**kwargs)


@dataclass
class Disease(YAMLRoot):
    """
    List of Disease Ontology terms used to describe diseases recorded in association with C2M2 subjects or biosamples
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.Disease
    class_class_curie: ClassVar[str] = "cfde_schema:Disease"
    class_name: ClassVar[str] = "disease"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.Disease

    id: Union[str, DiseaseId] = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseId):
            self.id = DiseaseId(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        super().__post_init__(**kwargs)


@dataclass
class Phenotype(YAMLRoot):
    """
    List of Human Phenotype Ontology terms used to describe phenotypes recorded in association with C2M2 subjects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.Phenotype
    class_class_curie: ClassVar[str] = "cfde_schema:Phenotype"
    class_name: ClassVar[str] = "phenotype"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.Phenotype

    id: Union[str, PhenotypeId] = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhenotypeId):
            self.id = PhenotypeId(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        super().__post_init__(**kwargs)


@dataclass
class Compound(YAMLRoot):
    """
    List of (i) GlyTouCan terms or (ii) PubChem 'compound' terms (normalized chemical structures) referenced in this
    submission; (ii) will include all PubChem 'compound' terms associated with any PubChem 'substance' terms (specific
    formulations of chemical materials) directly referenced in this submission, in addition to any 'compound' terms
    directly referenced
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.Compound
    class_class_curie: ClassVar[str] = "cfde_schema:Compound"
    class_name: ClassVar[str] = "compound"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.Compound

    id: Union[str, CompoundId] = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundId):
            self.id = CompoundId(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        super().__post_init__(**kwargs)


@dataclass
class Substance(YAMLRoot):
    """
    List of PubChem 'substance' terms (specific formulations of chemical materials) directly referenced in this C2M2
    submission
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.Substance
    class_class_curie: ClassVar[str] = "cfde_schema:Substance"
    class_name: ClassVar[str] = "substance"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.Substance

    id: Union[str, SubstanceId] = None
    compound: Union[str, CompoundId] = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SubstanceId):
            self.id = SubstanceId(self.id)

        if self._is_empty(self.compound):
            self.MissingRequiredField("compound")
        if not isinstance(self.compound, CompoundId):
            self.compound = CompoundId(self.compound)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        super().__post_init__(**kwargs)


@dataclass
class Gene(YAMLRoot):
    """
    List of Ensembl genes directly referenced in this C2M2 submission
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.Gene
    class_class_curie: ClassVar[str] = "cfde_schema:Gene"
    class_name: ClassVar[str] = "gene"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.Gene

    id: Union[str, GeneId] = None
    organism: Union[str, NcbiTaxonomyId] = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneId):
            self.id = GeneId(self.id)

        if self._is_empty(self.organism):
            self.MissingRequiredField("organism")
        if not isinstance(self.organism, NcbiTaxonomyId):
            self.organism = NcbiTaxonomyId(self.organism)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        super().__post_init__(**kwargs)


@dataclass
class Protein(YAMLRoot):
    """
    List of UniProtKB proteins directly referenced in this C2M2 submission
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.Protein
    class_class_curie: ClassVar[str] = "cfde_schema:Protein"
    class_name: ClassVar[str] = "protein"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.Protein

    id: Union[str, ProteinId] = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()
    organism: Optional[Union[str, NcbiTaxonomyId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProteinId):
            self.id = ProteinId(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        if self.organism is not None and not isinstance(self.organism, NcbiTaxonomyId):
            self.organism = NcbiTaxonomyId(self.organism)

        super().__post_init__(**kwargs)


@dataclass
class ProteinGene(YAMLRoot):
    """
    Association between a UniProtKB protein term and an Ensembl term identifying a gene encoding that protein
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.ProteinGene
    class_class_curie: ClassVar[str] = "cfde_schema:ProteinGene"
    class_name: ClassVar[str] = "protein_gene"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.ProteinGene

    protein: Union[str, ProteinId] = None
    gene: Union[str, GeneId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.protein):
            self.MissingRequiredField("protein")
        if not isinstance(self.protein, ProteinId):
            self.protein = ProteinId(self.protein)

        if self._is_empty(self.gene):
            self.MissingRequiredField("gene")
        if not isinstance(self.gene, GeneId):
            self.gene = GeneId(self.gene)

        super().__post_init__(**kwargs)


@dataclass
class IdNamespace(YAMLRoot):
    """
    A table listing identifier namespaces registered by the DCC submitting this C2M2 instance
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CFDE_SCHEMA.IdNamespace
    class_class_curie: ClassVar[str] = "cfde_schema:IdNamespace"
    class_name: ClassVar[str] = "id_namespace"
    class_model_uri: ClassVar[URIRef] = CFDE_SCHEMA.IdNamespace

    id: Union[str, IdNamespaceId] = None
    abbreviation: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IdNamespaceId):
            self.id = IdNamespaceId(self.id)

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

slots.file__id_namespace = Slot(uri=CFDE_SCHEMA.id_namespace, name="file__id_namespace", curie=CFDE_SCHEMA.curie('id_namespace'),
                   model_uri=CFDE_SCHEMA.file__id_namespace, domain=None, range=Union[str, IdNamespaceId])

slots.file__local_id = Slot(uri=CFDE_SCHEMA.local_id, name="file__local_id", curie=CFDE_SCHEMA.curie('local_id'),
                   model_uri=CFDE_SCHEMA.file__local_id, domain=None, range=str)

slots.file__project_id_namespace = Slot(uri=CFDE_SCHEMA.project_id_namespace, name="file__project_id_namespace", curie=CFDE_SCHEMA.curie('project_id_namespace'),
                   model_uri=CFDE_SCHEMA.file__project_id_namespace, domain=None, range=str)

slots.file__project_local_id = Slot(uri=CFDE_SCHEMA.project_local_id, name="file__project_local_id", curie=CFDE_SCHEMA.curie('project_local_id'),
                   model_uri=CFDE_SCHEMA.file__project_local_id, domain=None, range=str)

slots.file__persistent_id = Slot(uri=CFDE_SCHEMA.persistent_id, name="file__persistent_id", curie=CFDE_SCHEMA.curie('persistent_id'),
                   model_uri=CFDE_SCHEMA.file__persistent_id, domain=None, range=Optional[str])

slots.file__creation_time = Slot(uri=CFDE_SCHEMA.creation_time, name="file__creation_time", curie=CFDE_SCHEMA.curie('creation_time'),
                   model_uri=CFDE_SCHEMA.file__creation_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.file__size_in_bytes = Slot(uri=CFDE_SCHEMA.size_in_bytes, name="file__size_in_bytes", curie=CFDE_SCHEMA.curie('size_in_bytes'),
                   model_uri=CFDE_SCHEMA.file__size_in_bytes, domain=None, range=Optional[int])

slots.file__uncompressed_size_in_bytes = Slot(uri=CFDE_SCHEMA.uncompressed_size_in_bytes, name="file__uncompressed_size_in_bytes", curie=CFDE_SCHEMA.curie('uncompressed_size_in_bytes'),
                   model_uri=CFDE_SCHEMA.file__uncompressed_size_in_bytes, domain=None, range=Optional[int])

slots.file__sha256 = Slot(uri=CFDE_SCHEMA.sha256, name="file__sha256", curie=CFDE_SCHEMA.curie('sha256'),
                   model_uri=CFDE_SCHEMA.file__sha256, domain=None, range=Optional[str])

slots.file__md5 = Slot(uri=CFDE_SCHEMA.md5, name="file__md5", curie=CFDE_SCHEMA.curie('md5'),
                   model_uri=CFDE_SCHEMA.file__md5, domain=None, range=Optional[str])

slots.file__filename = Slot(uri=CFDE_SCHEMA.filename, name="file__filename", curie=CFDE_SCHEMA.curie('filename'),
                   model_uri=CFDE_SCHEMA.file__filename, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[^/\:]+$'))

slots.file__file_format = Slot(uri=CFDE_SCHEMA.file_format, name="file__file_format", curie=CFDE_SCHEMA.curie('file_format'),
                   model_uri=CFDE_SCHEMA.file__file_format, domain=None, range=Optional[Union[str, FileFormatId]])

slots.file__compression_format = Slot(uri=CFDE_SCHEMA.compression_format, name="file__compression_format", curie=CFDE_SCHEMA.curie('compression_format'),
                   model_uri=CFDE_SCHEMA.file__compression_format, domain=None, range=Optional[Union[str, FileFormatId]])

slots.file__data_type = Slot(uri=CFDE_SCHEMA.data_type, name="file__data_type", curie=CFDE_SCHEMA.curie('data_type'),
                   model_uri=CFDE_SCHEMA.file__data_type, domain=None, range=Optional[Union[str, DataTypeId]])

slots.file__assay_type = Slot(uri=CFDE_SCHEMA.assay_type, name="file__assay_type", curie=CFDE_SCHEMA.curie('assay_type'),
                   model_uri=CFDE_SCHEMA.file__assay_type, domain=None, range=Optional[Union[str, AssayTypeId]])

slots.file__analysis_type = Slot(uri=CFDE_SCHEMA.analysis_type, name="file__analysis_type", curie=CFDE_SCHEMA.curie('analysis_type'),
                   model_uri=CFDE_SCHEMA.file__analysis_type, domain=None, range=Optional[Union[str, AnalysisTypeId]])

slots.file__mime_type = Slot(uri=CFDE_SCHEMA.mime_type, name="file__mime_type", curie=CFDE_SCHEMA.curie('mime_type'),
                   model_uri=CFDE_SCHEMA.file__mime_type, domain=None, range=Optional[str])

slots.file__bundle_collection_id_namespace = Slot(uri=CFDE_SCHEMA.bundle_collection_id_namespace, name="file__bundle_collection_id_namespace", curie=CFDE_SCHEMA.curie('bundle_collection_id_namespace'),
                   model_uri=CFDE_SCHEMA.file__bundle_collection_id_namespace, domain=None, range=Optional[str])

slots.file__bundle_collection_local_id = Slot(uri=CFDE_SCHEMA.bundle_collection_local_id, name="file__bundle_collection_local_id", curie=CFDE_SCHEMA.curie('bundle_collection_local_id'),
                   model_uri=CFDE_SCHEMA.file__bundle_collection_local_id, domain=None, range=Optional[str])

slots.file__dbgap_study_id = Slot(uri=CFDE_SCHEMA.dbgap_study_id, name="file__dbgap_study_id", curie=CFDE_SCHEMA.curie('dbgap_study_id'),
                   model_uri=CFDE_SCHEMA.file__dbgap_study_id, domain=None, range=Optional[str])

slots.biosample__id_namespace = Slot(uri=CFDE_SCHEMA.id_namespace, name="biosample__id_namespace", curie=CFDE_SCHEMA.curie('id_namespace'),
                   model_uri=CFDE_SCHEMA.biosample__id_namespace, domain=None, range=Union[str, IdNamespaceId])

slots.biosample__local_id = Slot(uri=CFDE_SCHEMA.local_id, name="biosample__local_id", curie=CFDE_SCHEMA.curie('local_id'),
                   model_uri=CFDE_SCHEMA.biosample__local_id, domain=None, range=str)

slots.biosample__project_id_namespace = Slot(uri=CFDE_SCHEMA.project_id_namespace, name="biosample__project_id_namespace", curie=CFDE_SCHEMA.curie('project_id_namespace'),
                   model_uri=CFDE_SCHEMA.biosample__project_id_namespace, domain=None, range=str)

slots.biosample__project_local_id = Slot(uri=CFDE_SCHEMA.project_local_id, name="biosample__project_local_id", curie=CFDE_SCHEMA.curie('project_local_id'),
                   model_uri=CFDE_SCHEMA.biosample__project_local_id, domain=None, range=str)

slots.biosample__persistent_id = Slot(uri=CFDE_SCHEMA.persistent_id, name="biosample__persistent_id", curie=CFDE_SCHEMA.curie('persistent_id'),
                   model_uri=CFDE_SCHEMA.biosample__persistent_id, domain=None, range=Optional[str])

slots.biosample__creation_time = Slot(uri=CFDE_SCHEMA.creation_time, name="biosample__creation_time", curie=CFDE_SCHEMA.curie('creation_time'),
                   model_uri=CFDE_SCHEMA.biosample__creation_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.biosample__assay_type = Slot(uri=CFDE_SCHEMA.assay_type, name="biosample__assay_type", curie=CFDE_SCHEMA.curie('assay_type'),
                   model_uri=CFDE_SCHEMA.biosample__assay_type, domain=None, range=Optional[Union[str, AssayTypeId]])

slots.biosample__anatomy = Slot(uri=CFDE_SCHEMA.anatomy, name="biosample__anatomy", curie=CFDE_SCHEMA.curie('anatomy'),
                   model_uri=CFDE_SCHEMA.biosample__anatomy, domain=None, range=Optional[Union[str, AnatomyId]])

slots.subject__id_namespace = Slot(uri=CFDE_SCHEMA.id_namespace, name="subject__id_namespace", curie=CFDE_SCHEMA.curie('id_namespace'),
                   model_uri=CFDE_SCHEMA.subject__id_namespace, domain=None, range=Union[str, IdNamespaceId])

slots.subject__local_id = Slot(uri=CFDE_SCHEMA.local_id, name="subject__local_id", curie=CFDE_SCHEMA.curie('local_id'),
                   model_uri=CFDE_SCHEMA.subject__local_id, domain=None, range=str)

slots.subject__project_id_namespace = Slot(uri=CFDE_SCHEMA.project_id_namespace, name="subject__project_id_namespace", curie=CFDE_SCHEMA.curie('project_id_namespace'),
                   model_uri=CFDE_SCHEMA.subject__project_id_namespace, domain=None, range=str)

slots.subject__project_local_id = Slot(uri=CFDE_SCHEMA.project_local_id, name="subject__project_local_id", curie=CFDE_SCHEMA.curie('project_local_id'),
                   model_uri=CFDE_SCHEMA.subject__project_local_id, domain=None, range=str)

slots.subject__persistent_id = Slot(uri=CFDE_SCHEMA.persistent_id, name="subject__persistent_id", curie=CFDE_SCHEMA.curie('persistent_id'),
                   model_uri=CFDE_SCHEMA.subject__persistent_id, domain=None, range=Optional[str])

slots.subject__creation_time = Slot(uri=CFDE_SCHEMA.creation_time, name="subject__creation_time", curie=CFDE_SCHEMA.curie('creation_time'),
                   model_uri=CFDE_SCHEMA.subject__creation_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.subject__granularity = Slot(uri=CFDE_SCHEMA.granularity, name="subject__granularity", curie=CFDE_SCHEMA.curie('granularity'),
                   model_uri=CFDE_SCHEMA.subject__granularity, domain=None, range=Union[str, "GranularityEnum"])

slots.subject__sex = Slot(uri=CFDE_SCHEMA.sex, name="subject__sex", curie=CFDE_SCHEMA.curie('sex'),
                   model_uri=CFDE_SCHEMA.subject__sex, domain=None, range=Optional[Union[str, "SexEnum"]])

slots.subject__ethnicity = Slot(uri=CFDE_SCHEMA.ethnicity, name="subject__ethnicity", curie=CFDE_SCHEMA.curie('ethnicity'),
                   model_uri=CFDE_SCHEMA.subject__ethnicity, domain=None, range=Optional[Union[str, "EthnicityEnum"]])

slots.subject__age_at_enrollment = Slot(uri=CFDE_SCHEMA.age_at_enrollment, name="subject__age_at_enrollment", curie=CFDE_SCHEMA.curie('age_at_enrollment'),
                   model_uri=CFDE_SCHEMA.subject__age_at_enrollment, domain=None, range=Optional[Decimal])

slots.dcc__id = Slot(uri=CFDE_SCHEMA.id, name="dcc__id", curie=CFDE_SCHEMA.curie('id'),
                   model_uri=CFDE_SCHEMA.dcc__id, domain=None, range=URIRef)

slots.dcc__dcc_name = Slot(uri=CFDE_SCHEMA.dcc_name, name="dcc__dcc_name", curie=CFDE_SCHEMA.curie('dcc_name'),
                   model_uri=CFDE_SCHEMA.dcc__dcc_name, domain=None, range=str)

slots.dcc__dcc_abbreviation = Slot(uri=CFDE_SCHEMA.dcc_abbreviation, name="dcc__dcc_abbreviation", curie=CFDE_SCHEMA.curie('dcc_abbreviation'),
                   model_uri=CFDE_SCHEMA.dcc__dcc_abbreviation, domain=None, range=str,
                   pattern=re.compile(r'^[a-zA-Z0-9_]+$'))

slots.dcc__dcc_description = Slot(uri=CFDE_SCHEMA.dcc_description, name="dcc__dcc_description", curie=CFDE_SCHEMA.curie('dcc_description'),
                   model_uri=CFDE_SCHEMA.dcc__dcc_description, domain=None, range=Optional[str])

slots.dcc__contact_email = Slot(uri=CFDE_SCHEMA.contact_email, name="dcc__contact_email", curie=CFDE_SCHEMA.curie('contact_email'),
                   model_uri=CFDE_SCHEMA.dcc__contact_email, domain=None, range=str)

slots.dcc__contact_name = Slot(uri=CFDE_SCHEMA.contact_name, name="dcc__contact_name", curie=CFDE_SCHEMA.curie('contact_name'),
                   model_uri=CFDE_SCHEMA.dcc__contact_name, domain=None, range=str)

slots.dcc__dcc_url = Slot(uri=CFDE_SCHEMA.dcc_url, name="dcc__dcc_url", curie=CFDE_SCHEMA.curie('dcc_url'),
                   model_uri=CFDE_SCHEMA.dcc__dcc_url, domain=None, range=str)

slots.dcc__project_id_namespace = Slot(uri=CFDE_SCHEMA.project_id_namespace, name="dcc__project_id_namespace", curie=CFDE_SCHEMA.curie('project_id_namespace'),
                   model_uri=CFDE_SCHEMA.dcc__project_id_namespace, domain=None, range=str)

slots.dcc__project_local_id = Slot(uri=CFDE_SCHEMA.project_local_id, name="dcc__project_local_id", curie=CFDE_SCHEMA.curie('project_local_id'),
                   model_uri=CFDE_SCHEMA.dcc__project_local_id, domain=None, range=str)

slots.project__id_namespace = Slot(uri=CFDE_SCHEMA.id_namespace, name="project__id_namespace", curie=CFDE_SCHEMA.curie('id_namespace'),
                   model_uri=CFDE_SCHEMA.project__id_namespace, domain=None, range=Union[str, IdNamespaceId])

slots.project__local_id = Slot(uri=CFDE_SCHEMA.local_id, name="project__local_id", curie=CFDE_SCHEMA.curie('local_id'),
                   model_uri=CFDE_SCHEMA.project__local_id, domain=None, range=str)

slots.project__persistent_id = Slot(uri=CFDE_SCHEMA.persistent_id, name="project__persistent_id", curie=CFDE_SCHEMA.curie('persistent_id'),
                   model_uri=CFDE_SCHEMA.project__persistent_id, domain=None, range=Optional[str])

slots.project__creation_time = Slot(uri=CFDE_SCHEMA.creation_time, name="project__creation_time", curie=CFDE_SCHEMA.curie('creation_time'),
                   model_uri=CFDE_SCHEMA.project__creation_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.project__abbreviation = Slot(uri=CFDE_SCHEMA.abbreviation, name="project__abbreviation", curie=CFDE_SCHEMA.curie('abbreviation'),
                   model_uri=CFDE_SCHEMA.project__abbreviation, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-zA-Z0-9_]+$'))

slots.project__description = Slot(uri=CFDE_SCHEMA.description, name="project__description", curie=CFDE_SCHEMA.curie('description'),
                   model_uri=CFDE_SCHEMA.project__description, domain=None, range=Optional[str])

slots.projectInProject__parent_project_id_namespace = Slot(uri=CFDE_SCHEMA.parent_project_id_namespace, name="projectInProject__parent_project_id_namespace", curie=CFDE_SCHEMA.curie('parent_project_id_namespace'),
                   model_uri=CFDE_SCHEMA.projectInProject__parent_project_id_namespace, domain=None, range=str)

slots.projectInProject__parent_project_local_id = Slot(uri=CFDE_SCHEMA.parent_project_local_id, name="projectInProject__parent_project_local_id", curie=CFDE_SCHEMA.curie('parent_project_local_id'),
                   model_uri=CFDE_SCHEMA.projectInProject__parent_project_local_id, domain=None, range=str)

slots.projectInProject__child_project_id_namespace = Slot(uri=CFDE_SCHEMA.child_project_id_namespace, name="projectInProject__child_project_id_namespace", curie=CFDE_SCHEMA.curie('child_project_id_namespace'),
                   model_uri=CFDE_SCHEMA.projectInProject__child_project_id_namespace, domain=None, range=str)

slots.projectInProject__child_project_local_id = Slot(uri=CFDE_SCHEMA.child_project_local_id, name="projectInProject__child_project_local_id", curie=CFDE_SCHEMA.curie('child_project_local_id'),
                   model_uri=CFDE_SCHEMA.projectInProject__child_project_local_id, domain=None, range=str)

slots.collection__id_namespace = Slot(uri=CFDE_SCHEMA.id_namespace, name="collection__id_namespace", curie=CFDE_SCHEMA.curie('id_namespace'),
                   model_uri=CFDE_SCHEMA.collection__id_namespace, domain=None, range=Union[str, IdNamespaceId])

slots.collection__local_id = Slot(uri=CFDE_SCHEMA.local_id, name="collection__local_id", curie=CFDE_SCHEMA.curie('local_id'),
                   model_uri=CFDE_SCHEMA.collection__local_id, domain=None, range=str)

slots.collection__persistent_id = Slot(uri=CFDE_SCHEMA.persistent_id, name="collection__persistent_id", curie=CFDE_SCHEMA.curie('persistent_id'),
                   model_uri=CFDE_SCHEMA.collection__persistent_id, domain=None, range=Optional[str])

slots.collection__creation_time = Slot(uri=CFDE_SCHEMA.creation_time, name="collection__creation_time", curie=CFDE_SCHEMA.curie('creation_time'),
                   model_uri=CFDE_SCHEMA.collection__creation_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.collection__abbreviation = Slot(uri=CFDE_SCHEMA.abbreviation, name="collection__abbreviation", curie=CFDE_SCHEMA.curie('abbreviation'),
                   model_uri=CFDE_SCHEMA.collection__abbreviation, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-zA-Z0-9_]+$'))

slots.collection__description = Slot(uri=CFDE_SCHEMA.description, name="collection__description", curie=CFDE_SCHEMA.curie('description'),
                   model_uri=CFDE_SCHEMA.collection__description, domain=None, range=Optional[str])

slots.collection__has_time_series_data = Slot(uri=CFDE_SCHEMA.has_time_series_data, name="collection__has_time_series_data", curie=CFDE_SCHEMA.curie('has_time_series_data'),
                   model_uri=CFDE_SCHEMA.collection__has_time_series_data, domain=None, range=Optional[Union[bool, Bool]])

slots.collectionInCollection__superset_collection_id_namespace = Slot(uri=CFDE_SCHEMA.superset_collection_id_namespace, name="collectionInCollection__superset_collection_id_namespace", curie=CFDE_SCHEMA.curie('superset_collection_id_namespace'),
                   model_uri=CFDE_SCHEMA.collectionInCollection__superset_collection_id_namespace, domain=None, range=str)

slots.collectionInCollection__superset_collection_local_id = Slot(uri=CFDE_SCHEMA.superset_collection_local_id, name="collectionInCollection__superset_collection_local_id", curie=CFDE_SCHEMA.curie('superset_collection_local_id'),
                   model_uri=CFDE_SCHEMA.collectionInCollection__superset_collection_local_id, domain=None, range=str)

slots.collectionInCollection__subset_collection_id_namespace = Slot(uri=CFDE_SCHEMA.subset_collection_id_namespace, name="collectionInCollection__subset_collection_id_namespace", curie=CFDE_SCHEMA.curie('subset_collection_id_namespace'),
                   model_uri=CFDE_SCHEMA.collectionInCollection__subset_collection_id_namespace, domain=None, range=str)

slots.collectionInCollection__subset_collection_local_id = Slot(uri=CFDE_SCHEMA.subset_collection_local_id, name="collectionInCollection__subset_collection_local_id", curie=CFDE_SCHEMA.curie('subset_collection_local_id'),
                   model_uri=CFDE_SCHEMA.collectionInCollection__subset_collection_local_id, domain=None, range=str)

slots.fileDescribesCollection__file_id_namespace = Slot(uri=CFDE_SCHEMA.file_id_namespace, name="fileDescribesCollection__file_id_namespace", curie=CFDE_SCHEMA.curie('file_id_namespace'),
                   model_uri=CFDE_SCHEMA.fileDescribesCollection__file_id_namespace, domain=None, range=str)

slots.fileDescribesCollection__file_local_id = Slot(uri=CFDE_SCHEMA.file_local_id, name="fileDescribesCollection__file_local_id", curie=CFDE_SCHEMA.curie('file_local_id'),
                   model_uri=CFDE_SCHEMA.fileDescribesCollection__file_local_id, domain=None, range=str)

slots.fileDescribesCollection__collection_id_namespace = Slot(uri=CFDE_SCHEMA.collection_id_namespace, name="fileDescribesCollection__collection_id_namespace", curie=CFDE_SCHEMA.curie('collection_id_namespace'),
                   model_uri=CFDE_SCHEMA.fileDescribesCollection__collection_id_namespace, domain=None, range=str)

slots.fileDescribesCollection__collection_local_id = Slot(uri=CFDE_SCHEMA.collection_local_id, name="fileDescribesCollection__collection_local_id", curie=CFDE_SCHEMA.curie('collection_local_id'),
                   model_uri=CFDE_SCHEMA.fileDescribesCollection__collection_local_id, domain=None, range=str)

slots.collectionDefinedByProject__collection_id_namespace = Slot(uri=CFDE_SCHEMA.collection_id_namespace, name="collectionDefinedByProject__collection_id_namespace", curie=CFDE_SCHEMA.curie('collection_id_namespace'),
                   model_uri=CFDE_SCHEMA.collectionDefinedByProject__collection_id_namespace, domain=None, range=str)

slots.collectionDefinedByProject__collection_local_id = Slot(uri=CFDE_SCHEMA.collection_local_id, name="collectionDefinedByProject__collection_local_id", curie=CFDE_SCHEMA.curie('collection_local_id'),
                   model_uri=CFDE_SCHEMA.collectionDefinedByProject__collection_local_id, domain=None, range=str)

slots.collectionDefinedByProject__project_id_namespace = Slot(uri=CFDE_SCHEMA.project_id_namespace, name="collectionDefinedByProject__project_id_namespace", curie=CFDE_SCHEMA.curie('project_id_namespace'),
                   model_uri=CFDE_SCHEMA.collectionDefinedByProject__project_id_namespace, domain=None, range=str)

slots.collectionDefinedByProject__project_local_id = Slot(uri=CFDE_SCHEMA.project_local_id, name="collectionDefinedByProject__project_local_id", curie=CFDE_SCHEMA.curie('project_local_id'),
                   model_uri=CFDE_SCHEMA.collectionDefinedByProject__project_local_id, domain=None, range=str)

slots.fileInCollection__file_id_namespace = Slot(uri=CFDE_SCHEMA.file_id_namespace, name="fileInCollection__file_id_namespace", curie=CFDE_SCHEMA.curie('file_id_namespace'),
                   model_uri=CFDE_SCHEMA.fileInCollection__file_id_namespace, domain=None, range=str)

slots.fileInCollection__file_local_id = Slot(uri=CFDE_SCHEMA.file_local_id, name="fileInCollection__file_local_id", curie=CFDE_SCHEMA.curie('file_local_id'),
                   model_uri=CFDE_SCHEMA.fileInCollection__file_local_id, domain=None, range=str)

slots.fileInCollection__collection_id_namespace = Slot(uri=CFDE_SCHEMA.collection_id_namespace, name="fileInCollection__collection_id_namespace", curie=CFDE_SCHEMA.curie('collection_id_namespace'),
                   model_uri=CFDE_SCHEMA.fileInCollection__collection_id_namespace, domain=None, range=str)

slots.fileInCollection__collection_local_id = Slot(uri=CFDE_SCHEMA.collection_local_id, name="fileInCollection__collection_local_id", curie=CFDE_SCHEMA.curie('collection_local_id'),
                   model_uri=CFDE_SCHEMA.fileInCollection__collection_local_id, domain=None, range=str)

slots.biosampleInCollection__biosample_id_namespace = Slot(uri=CFDE_SCHEMA.biosample_id_namespace, name="biosampleInCollection__biosample_id_namespace", curie=CFDE_SCHEMA.curie('biosample_id_namespace'),
                   model_uri=CFDE_SCHEMA.biosampleInCollection__biosample_id_namespace, domain=None, range=str)

slots.biosampleInCollection__biosample_local_id = Slot(uri=CFDE_SCHEMA.biosample_local_id, name="biosampleInCollection__biosample_local_id", curie=CFDE_SCHEMA.curie('biosample_local_id'),
                   model_uri=CFDE_SCHEMA.biosampleInCollection__biosample_local_id, domain=None, range=str)

slots.biosampleInCollection__collection_id_namespace = Slot(uri=CFDE_SCHEMA.collection_id_namespace, name="biosampleInCollection__collection_id_namespace", curie=CFDE_SCHEMA.curie('collection_id_namespace'),
                   model_uri=CFDE_SCHEMA.biosampleInCollection__collection_id_namespace, domain=None, range=str)

slots.biosampleInCollection__collection_local_id = Slot(uri=CFDE_SCHEMA.collection_local_id, name="biosampleInCollection__collection_local_id", curie=CFDE_SCHEMA.curie('collection_local_id'),
                   model_uri=CFDE_SCHEMA.biosampleInCollection__collection_local_id, domain=None, range=str)

slots.subjectInCollection__subject_id_namespace = Slot(uri=CFDE_SCHEMA.subject_id_namespace, name="subjectInCollection__subject_id_namespace", curie=CFDE_SCHEMA.curie('subject_id_namespace'),
                   model_uri=CFDE_SCHEMA.subjectInCollection__subject_id_namespace, domain=None, range=str)

slots.subjectInCollection__subject_local_id = Slot(uri=CFDE_SCHEMA.subject_local_id, name="subjectInCollection__subject_local_id", curie=CFDE_SCHEMA.curie('subject_local_id'),
                   model_uri=CFDE_SCHEMA.subjectInCollection__subject_local_id, domain=None, range=str)

slots.subjectInCollection__collection_id_namespace = Slot(uri=CFDE_SCHEMA.collection_id_namespace, name="subjectInCollection__collection_id_namespace", curie=CFDE_SCHEMA.curie('collection_id_namespace'),
                   model_uri=CFDE_SCHEMA.subjectInCollection__collection_id_namespace, domain=None, range=str)

slots.subjectInCollection__collection_local_id = Slot(uri=CFDE_SCHEMA.collection_local_id, name="subjectInCollection__collection_local_id", curie=CFDE_SCHEMA.curie('collection_local_id'),
                   model_uri=CFDE_SCHEMA.subjectInCollection__collection_local_id, domain=None, range=str)

slots.fileDescribesBiosample__file_id_namespace = Slot(uri=CFDE_SCHEMA.file_id_namespace, name="fileDescribesBiosample__file_id_namespace", curie=CFDE_SCHEMA.curie('file_id_namespace'),
                   model_uri=CFDE_SCHEMA.fileDescribesBiosample__file_id_namespace, domain=None, range=str)

slots.fileDescribesBiosample__file_local_id = Slot(uri=CFDE_SCHEMA.file_local_id, name="fileDescribesBiosample__file_local_id", curie=CFDE_SCHEMA.curie('file_local_id'),
                   model_uri=CFDE_SCHEMA.fileDescribesBiosample__file_local_id, domain=None, range=str)

slots.fileDescribesBiosample__biosample_id_namespace = Slot(uri=CFDE_SCHEMA.biosample_id_namespace, name="fileDescribesBiosample__biosample_id_namespace", curie=CFDE_SCHEMA.curie('biosample_id_namespace'),
                   model_uri=CFDE_SCHEMA.fileDescribesBiosample__biosample_id_namespace, domain=None, range=str)

slots.fileDescribesBiosample__biosample_local_id = Slot(uri=CFDE_SCHEMA.biosample_local_id, name="fileDescribesBiosample__biosample_local_id", curie=CFDE_SCHEMA.curie('biosample_local_id'),
                   model_uri=CFDE_SCHEMA.fileDescribesBiosample__biosample_local_id, domain=None, range=str)

slots.fileDescribesSubject__file_id_namespace = Slot(uri=CFDE_SCHEMA.file_id_namespace, name="fileDescribesSubject__file_id_namespace", curie=CFDE_SCHEMA.curie('file_id_namespace'),
                   model_uri=CFDE_SCHEMA.fileDescribesSubject__file_id_namespace, domain=None, range=str)

slots.fileDescribesSubject__file_local_id = Slot(uri=CFDE_SCHEMA.file_local_id, name="fileDescribesSubject__file_local_id", curie=CFDE_SCHEMA.curie('file_local_id'),
                   model_uri=CFDE_SCHEMA.fileDescribesSubject__file_local_id, domain=None, range=str)

slots.fileDescribesSubject__subject_id_namespace = Slot(uri=CFDE_SCHEMA.subject_id_namespace, name="fileDescribesSubject__subject_id_namespace", curie=CFDE_SCHEMA.curie('subject_id_namespace'),
                   model_uri=CFDE_SCHEMA.fileDescribesSubject__subject_id_namespace, domain=None, range=str)

slots.fileDescribesSubject__subject_local_id = Slot(uri=CFDE_SCHEMA.subject_local_id, name="fileDescribesSubject__subject_local_id", curie=CFDE_SCHEMA.curie('subject_local_id'),
                   model_uri=CFDE_SCHEMA.fileDescribesSubject__subject_local_id, domain=None, range=str)

slots.biosampleFromSubject__biosample_id_namespace = Slot(uri=CFDE_SCHEMA.biosample_id_namespace, name="biosampleFromSubject__biosample_id_namespace", curie=CFDE_SCHEMA.curie('biosample_id_namespace'),
                   model_uri=CFDE_SCHEMA.biosampleFromSubject__biosample_id_namespace, domain=None, range=str)

slots.biosampleFromSubject__biosample_local_id = Slot(uri=CFDE_SCHEMA.biosample_local_id, name="biosampleFromSubject__biosample_local_id", curie=CFDE_SCHEMA.curie('biosample_local_id'),
                   model_uri=CFDE_SCHEMA.biosampleFromSubject__biosample_local_id, domain=None, range=str)

slots.biosampleFromSubject__subject_id_namespace = Slot(uri=CFDE_SCHEMA.subject_id_namespace, name="biosampleFromSubject__subject_id_namespace", curie=CFDE_SCHEMA.curie('subject_id_namespace'),
                   model_uri=CFDE_SCHEMA.biosampleFromSubject__subject_id_namespace, domain=None, range=str)

slots.biosampleFromSubject__subject_local_id = Slot(uri=CFDE_SCHEMA.subject_local_id, name="biosampleFromSubject__subject_local_id", curie=CFDE_SCHEMA.curie('subject_local_id'),
                   model_uri=CFDE_SCHEMA.biosampleFromSubject__subject_local_id, domain=None, range=str)

slots.biosampleFromSubject__age_at_sampling = Slot(uri=CFDE_SCHEMA.age_at_sampling, name="biosampleFromSubject__age_at_sampling", curie=CFDE_SCHEMA.curie('age_at_sampling'),
                   model_uri=CFDE_SCHEMA.biosampleFromSubject__age_at_sampling, domain=None, range=Optional[Decimal])

slots.biosampleDisease__biosample_id_namespace = Slot(uri=CFDE_SCHEMA.biosample_id_namespace, name="biosampleDisease__biosample_id_namespace", curie=CFDE_SCHEMA.curie('biosample_id_namespace'),
                   model_uri=CFDE_SCHEMA.biosampleDisease__biosample_id_namespace, domain=None, range=str)

slots.biosampleDisease__biosample_local_id = Slot(uri=CFDE_SCHEMA.biosample_local_id, name="biosampleDisease__biosample_local_id", curie=CFDE_SCHEMA.curie('biosample_local_id'),
                   model_uri=CFDE_SCHEMA.biosampleDisease__biosample_local_id, domain=None, range=str)

slots.biosampleDisease__association_type = Slot(uri=CFDE_SCHEMA.association_type, name="biosampleDisease__association_type", curie=CFDE_SCHEMA.curie('association_type'),
                   model_uri=CFDE_SCHEMA.biosampleDisease__association_type, domain=None, range=Union[str, "AssociationTypeEnum"])

slots.biosampleDisease__disease = Slot(uri=CFDE_SCHEMA.disease, name="biosampleDisease__disease", curie=CFDE_SCHEMA.curie('disease'),
                   model_uri=CFDE_SCHEMA.biosampleDisease__disease, domain=None, range=Union[str, DiseaseId])

slots.subjectDisease__subject_id_namespace = Slot(uri=CFDE_SCHEMA.subject_id_namespace, name="subjectDisease__subject_id_namespace", curie=CFDE_SCHEMA.curie('subject_id_namespace'),
                   model_uri=CFDE_SCHEMA.subjectDisease__subject_id_namespace, domain=None, range=str)

slots.subjectDisease__subject_local_id = Slot(uri=CFDE_SCHEMA.subject_local_id, name="subjectDisease__subject_local_id", curie=CFDE_SCHEMA.curie('subject_local_id'),
                   model_uri=CFDE_SCHEMA.subjectDisease__subject_local_id, domain=None, range=str)

slots.subjectDisease__association_type = Slot(uri=CFDE_SCHEMA.association_type, name="subjectDisease__association_type", curie=CFDE_SCHEMA.curie('association_type'),
                   model_uri=CFDE_SCHEMA.subjectDisease__association_type, domain=None, range=Union[str, "AssociationTypeEnum"])

slots.subjectDisease__disease = Slot(uri=CFDE_SCHEMA.disease, name="subjectDisease__disease", curie=CFDE_SCHEMA.curie('disease'),
                   model_uri=CFDE_SCHEMA.subjectDisease__disease, domain=None, range=Union[str, DiseaseId])

slots.collectionDisease__collection_id_namespace = Slot(uri=CFDE_SCHEMA.collection_id_namespace, name="collectionDisease__collection_id_namespace", curie=CFDE_SCHEMA.curie('collection_id_namespace'),
                   model_uri=CFDE_SCHEMA.collectionDisease__collection_id_namespace, domain=None, range=str)

slots.collectionDisease__collection_local_id = Slot(uri=CFDE_SCHEMA.collection_local_id, name="collectionDisease__collection_local_id", curie=CFDE_SCHEMA.curie('collection_local_id'),
                   model_uri=CFDE_SCHEMA.collectionDisease__collection_local_id, domain=None, range=str)

slots.collectionDisease__disease = Slot(uri=CFDE_SCHEMA.disease, name="collectionDisease__disease", curie=CFDE_SCHEMA.curie('disease'),
                   model_uri=CFDE_SCHEMA.collectionDisease__disease, domain=None, range=Union[str, DiseaseId])

slots.collectionPhenotype__collection_id_namespace = Slot(uri=CFDE_SCHEMA.collection_id_namespace, name="collectionPhenotype__collection_id_namespace", curie=CFDE_SCHEMA.curie('collection_id_namespace'),
                   model_uri=CFDE_SCHEMA.collectionPhenotype__collection_id_namespace, domain=None, range=str)

slots.collectionPhenotype__collection_local_id = Slot(uri=CFDE_SCHEMA.collection_local_id, name="collectionPhenotype__collection_local_id", curie=CFDE_SCHEMA.curie('collection_local_id'),
                   model_uri=CFDE_SCHEMA.collectionPhenotype__collection_local_id, domain=None, range=str)

slots.collectionPhenotype__phenotype = Slot(uri=CFDE_SCHEMA.phenotype, name="collectionPhenotype__phenotype", curie=CFDE_SCHEMA.curie('phenotype'),
                   model_uri=CFDE_SCHEMA.collectionPhenotype__phenotype, domain=None, range=Union[str, PhenotypeId])

slots.collectionGene__collection_id_namespace = Slot(uri=CFDE_SCHEMA.collection_id_namespace, name="collectionGene__collection_id_namespace", curie=CFDE_SCHEMA.curie('collection_id_namespace'),
                   model_uri=CFDE_SCHEMA.collectionGene__collection_id_namespace, domain=None, range=str)

slots.collectionGene__collection_local_id = Slot(uri=CFDE_SCHEMA.collection_local_id, name="collectionGene__collection_local_id", curie=CFDE_SCHEMA.curie('collection_local_id'),
                   model_uri=CFDE_SCHEMA.collectionGene__collection_local_id, domain=None, range=str)

slots.collectionGene__gene = Slot(uri=CFDE_SCHEMA.gene, name="collectionGene__gene", curie=CFDE_SCHEMA.curie('gene'),
                   model_uri=CFDE_SCHEMA.collectionGene__gene, domain=None, range=Union[str, GeneId])

slots.collectionCompound__collection_id_namespace = Slot(uri=CFDE_SCHEMA.collection_id_namespace, name="collectionCompound__collection_id_namespace", curie=CFDE_SCHEMA.curie('collection_id_namespace'),
                   model_uri=CFDE_SCHEMA.collectionCompound__collection_id_namespace, domain=None, range=str)

slots.collectionCompound__collection_local_id = Slot(uri=CFDE_SCHEMA.collection_local_id, name="collectionCompound__collection_local_id", curie=CFDE_SCHEMA.curie('collection_local_id'),
                   model_uri=CFDE_SCHEMA.collectionCompound__collection_local_id, domain=None, range=str)

slots.collectionCompound__compound = Slot(uri=CFDE_SCHEMA.compound, name="collectionCompound__compound", curie=CFDE_SCHEMA.curie('compound'),
                   model_uri=CFDE_SCHEMA.collectionCompound__compound, domain=None, range=Union[str, CompoundId])

slots.collectionSubstance__collection_id_namespace = Slot(uri=CFDE_SCHEMA.collection_id_namespace, name="collectionSubstance__collection_id_namespace", curie=CFDE_SCHEMA.curie('collection_id_namespace'),
                   model_uri=CFDE_SCHEMA.collectionSubstance__collection_id_namespace, domain=None, range=str)

slots.collectionSubstance__collection_local_id = Slot(uri=CFDE_SCHEMA.collection_local_id, name="collectionSubstance__collection_local_id", curie=CFDE_SCHEMA.curie('collection_local_id'),
                   model_uri=CFDE_SCHEMA.collectionSubstance__collection_local_id, domain=None, range=str)

slots.collectionSubstance__substance = Slot(uri=CFDE_SCHEMA.substance, name="collectionSubstance__substance", curie=CFDE_SCHEMA.curie('substance'),
                   model_uri=CFDE_SCHEMA.collectionSubstance__substance, domain=None, range=Union[str, SubstanceId])

slots.collectionTaxonomy__collection_id_namespace = Slot(uri=CFDE_SCHEMA.collection_id_namespace, name="collectionTaxonomy__collection_id_namespace", curie=CFDE_SCHEMA.curie('collection_id_namespace'),
                   model_uri=CFDE_SCHEMA.collectionTaxonomy__collection_id_namespace, domain=None, range=str)

slots.collectionTaxonomy__collection_local_id = Slot(uri=CFDE_SCHEMA.collection_local_id, name="collectionTaxonomy__collection_local_id", curie=CFDE_SCHEMA.curie('collection_local_id'),
                   model_uri=CFDE_SCHEMA.collectionTaxonomy__collection_local_id, domain=None, range=str)

slots.collectionTaxonomy__taxon = Slot(uri=CFDE_SCHEMA.taxon, name="collectionTaxonomy__taxon", curie=CFDE_SCHEMA.curie('taxon'),
                   model_uri=CFDE_SCHEMA.collectionTaxonomy__taxon, domain=None, range=Union[str, NcbiTaxonomyId])

slots.collectionAnatomy__collection_id_namespace = Slot(uri=CFDE_SCHEMA.collection_id_namespace, name="collectionAnatomy__collection_id_namespace", curie=CFDE_SCHEMA.curie('collection_id_namespace'),
                   model_uri=CFDE_SCHEMA.collectionAnatomy__collection_id_namespace, domain=None, range=str)

slots.collectionAnatomy__collection_local_id = Slot(uri=CFDE_SCHEMA.collection_local_id, name="collectionAnatomy__collection_local_id", curie=CFDE_SCHEMA.curie('collection_local_id'),
                   model_uri=CFDE_SCHEMA.collectionAnatomy__collection_local_id, domain=None, range=str)

slots.collectionAnatomy__anatomy = Slot(uri=CFDE_SCHEMA.anatomy, name="collectionAnatomy__anatomy", curie=CFDE_SCHEMA.curie('anatomy'),
                   model_uri=CFDE_SCHEMA.collectionAnatomy__anatomy, domain=None, range=Union[str, AnatomyId])

slots.collectionProtein__collection_id_namespace = Slot(uri=CFDE_SCHEMA.collection_id_namespace, name="collectionProtein__collection_id_namespace", curie=CFDE_SCHEMA.curie('collection_id_namespace'),
                   model_uri=CFDE_SCHEMA.collectionProtein__collection_id_namespace, domain=None, range=str)

slots.collectionProtein__collection_local_id = Slot(uri=CFDE_SCHEMA.collection_local_id, name="collectionProtein__collection_local_id", curie=CFDE_SCHEMA.curie('collection_local_id'),
                   model_uri=CFDE_SCHEMA.collectionProtein__collection_local_id, domain=None, range=str)

slots.collectionProtein__protein = Slot(uri=CFDE_SCHEMA.protein, name="collectionProtein__protein", curie=CFDE_SCHEMA.curie('protein'),
                   model_uri=CFDE_SCHEMA.collectionProtein__protein, domain=None, range=Union[str, ProteinId])

slots.subjectPhenotype__subject_id_namespace = Slot(uri=CFDE_SCHEMA.subject_id_namespace, name="subjectPhenotype__subject_id_namespace", curie=CFDE_SCHEMA.curie('subject_id_namespace'),
                   model_uri=CFDE_SCHEMA.subjectPhenotype__subject_id_namespace, domain=None, range=str)

slots.subjectPhenotype__subject_local_id = Slot(uri=CFDE_SCHEMA.subject_local_id, name="subjectPhenotype__subject_local_id", curie=CFDE_SCHEMA.curie('subject_local_id'),
                   model_uri=CFDE_SCHEMA.subjectPhenotype__subject_local_id, domain=None, range=str)

slots.subjectPhenotype__association_type = Slot(uri=CFDE_SCHEMA.association_type, name="subjectPhenotype__association_type", curie=CFDE_SCHEMA.curie('association_type'),
                   model_uri=CFDE_SCHEMA.subjectPhenotype__association_type, domain=None, range=Union[str, "AssociationTypeEnum"])

slots.subjectPhenotype__phenotype = Slot(uri=CFDE_SCHEMA.phenotype, name="subjectPhenotype__phenotype", curie=CFDE_SCHEMA.curie('phenotype'),
                   model_uri=CFDE_SCHEMA.subjectPhenotype__phenotype, domain=None, range=Union[str, PhenotypeId])

slots.biosampleSubstance__biosample_id_namespace = Slot(uri=CFDE_SCHEMA.biosample_id_namespace, name="biosampleSubstance__biosample_id_namespace", curie=CFDE_SCHEMA.curie('biosample_id_namespace'),
                   model_uri=CFDE_SCHEMA.biosampleSubstance__biosample_id_namespace, domain=None, range=str)

slots.biosampleSubstance__biosample_local_id = Slot(uri=CFDE_SCHEMA.biosample_local_id, name="biosampleSubstance__biosample_local_id", curie=CFDE_SCHEMA.curie('biosample_local_id'),
                   model_uri=CFDE_SCHEMA.biosampleSubstance__biosample_local_id, domain=None, range=str)

slots.biosampleSubstance__substance = Slot(uri=CFDE_SCHEMA.substance, name="biosampleSubstance__substance", curie=CFDE_SCHEMA.curie('substance'),
                   model_uri=CFDE_SCHEMA.biosampleSubstance__substance, domain=None, range=Union[str, SubstanceId])

slots.subjectSubstance__subject_id_namespace = Slot(uri=CFDE_SCHEMA.subject_id_namespace, name="subjectSubstance__subject_id_namespace", curie=CFDE_SCHEMA.curie('subject_id_namespace'),
                   model_uri=CFDE_SCHEMA.subjectSubstance__subject_id_namespace, domain=None, range=str)

slots.subjectSubstance__subject_local_id = Slot(uri=CFDE_SCHEMA.subject_local_id, name="subjectSubstance__subject_local_id", curie=CFDE_SCHEMA.curie('subject_local_id'),
                   model_uri=CFDE_SCHEMA.subjectSubstance__subject_local_id, domain=None, range=str)

slots.subjectSubstance__substance = Slot(uri=CFDE_SCHEMA.substance, name="subjectSubstance__substance", curie=CFDE_SCHEMA.curie('substance'),
                   model_uri=CFDE_SCHEMA.subjectSubstance__substance, domain=None, range=Union[str, SubstanceId])

slots.biosampleGene__biosample_id_namespace = Slot(uri=CFDE_SCHEMA.biosample_id_namespace, name="biosampleGene__biosample_id_namespace", curie=CFDE_SCHEMA.curie('biosample_id_namespace'),
                   model_uri=CFDE_SCHEMA.biosampleGene__biosample_id_namespace, domain=None, range=str)

slots.biosampleGene__biosample_local_id = Slot(uri=CFDE_SCHEMA.biosample_local_id, name="biosampleGene__biosample_local_id", curie=CFDE_SCHEMA.curie('biosample_local_id'),
                   model_uri=CFDE_SCHEMA.biosampleGene__biosample_local_id, domain=None, range=str)

slots.biosampleGene__gene = Slot(uri=CFDE_SCHEMA.gene, name="biosampleGene__gene", curie=CFDE_SCHEMA.curie('gene'),
                   model_uri=CFDE_SCHEMA.biosampleGene__gene, domain=None, range=Union[str, GeneId])

slots.phenotypeGene__phenotype = Slot(uri=CFDE_SCHEMA.phenotype, name="phenotypeGene__phenotype", curie=CFDE_SCHEMA.curie('phenotype'),
                   model_uri=CFDE_SCHEMA.phenotypeGene__phenotype, domain=None, range=Union[str, PhenotypeId])

slots.phenotypeGene__gene = Slot(uri=CFDE_SCHEMA.gene, name="phenotypeGene__gene", curie=CFDE_SCHEMA.curie('gene'),
                   model_uri=CFDE_SCHEMA.phenotypeGene__gene, domain=None, range=Union[str, GeneId])

slots.phenotypeDisease__phenotype = Slot(uri=CFDE_SCHEMA.phenotype, name="phenotypeDisease__phenotype", curie=CFDE_SCHEMA.curie('phenotype'),
                   model_uri=CFDE_SCHEMA.phenotypeDisease__phenotype, domain=None, range=Union[str, PhenotypeId])

slots.phenotypeDisease__disease = Slot(uri=CFDE_SCHEMA.disease, name="phenotypeDisease__disease", curie=CFDE_SCHEMA.curie('disease'),
                   model_uri=CFDE_SCHEMA.phenotypeDisease__disease, domain=None, range=Union[str, DiseaseId])

slots.subjectRace__subject_id_namespace = Slot(uri=CFDE_SCHEMA.subject_id_namespace, name="subjectRace__subject_id_namespace", curie=CFDE_SCHEMA.curie('subject_id_namespace'),
                   model_uri=CFDE_SCHEMA.subjectRace__subject_id_namespace, domain=None, range=str)

slots.subjectRace__subject_local_id = Slot(uri=CFDE_SCHEMA.subject_local_id, name="subjectRace__subject_local_id", curie=CFDE_SCHEMA.curie('subject_local_id'),
                   model_uri=CFDE_SCHEMA.subjectRace__subject_local_id, domain=None, range=str)

slots.subjectRace__race = Slot(uri=CFDE_SCHEMA.race, name="subjectRace__race", curie=CFDE_SCHEMA.curie('race'),
                   model_uri=CFDE_SCHEMA.subjectRace__race, domain=None, range=Optional[Union[str, "RaceEnum"]])

slots.subjectRoleTaxonomy__subject_id_namespace = Slot(uri=CFDE_SCHEMA.subject_id_namespace, name="subjectRoleTaxonomy__subject_id_namespace", curie=CFDE_SCHEMA.curie('subject_id_namespace'),
                   model_uri=CFDE_SCHEMA.subjectRoleTaxonomy__subject_id_namespace, domain=None, range=str)

slots.subjectRoleTaxonomy__subject_local_id = Slot(uri=CFDE_SCHEMA.subject_local_id, name="subjectRoleTaxonomy__subject_local_id", curie=CFDE_SCHEMA.curie('subject_local_id'),
                   model_uri=CFDE_SCHEMA.subjectRoleTaxonomy__subject_local_id, domain=None, range=str)

slots.subjectRoleTaxonomy__role_id = Slot(uri=CFDE_SCHEMA.role_id, name="subjectRoleTaxonomy__role_id", curie=CFDE_SCHEMA.curie('role_id'),
                   model_uri=CFDE_SCHEMA.subjectRoleTaxonomy__role_id, domain=None, range=Union[str, "RoleIdEnum"])

slots.subjectRoleTaxonomy__taxonomy_id = Slot(uri=CFDE_SCHEMA.taxonomy_id, name="subjectRoleTaxonomy__taxonomy_id", curie=CFDE_SCHEMA.curie('taxonomy_id'),
                   model_uri=CFDE_SCHEMA.subjectRoleTaxonomy__taxonomy_id, domain=None, range=Union[str, NcbiTaxonomyId])

slots.assayType__id = Slot(uri=CFDE_SCHEMA.id, name="assayType__id", curie=CFDE_SCHEMA.curie('id'),
                   model_uri=CFDE_SCHEMA.assayType__id, domain=None, range=URIRef)

slots.assayType__description = Slot(uri=CFDE_SCHEMA.description, name="assayType__description", curie=CFDE_SCHEMA.curie('description'),
                   model_uri=CFDE_SCHEMA.assayType__description, domain=None, range=Optional[str])

slots.assayType__synonyms = Slot(uri=CFDE_SCHEMA.synonyms, name="assayType__synonyms", curie=CFDE_SCHEMA.curie('synonyms'),
                   model_uri=CFDE_SCHEMA.assayType__synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.analysisType__id = Slot(uri=CFDE_SCHEMA.id, name="analysisType__id", curie=CFDE_SCHEMA.curie('id'),
                   model_uri=CFDE_SCHEMA.analysisType__id, domain=None, range=URIRef)

slots.analysisType__description = Slot(uri=CFDE_SCHEMA.description, name="analysisType__description", curie=CFDE_SCHEMA.curie('description'),
                   model_uri=CFDE_SCHEMA.analysisType__description, domain=None, range=Optional[str])

slots.analysisType__synonyms = Slot(uri=CFDE_SCHEMA.synonyms, name="analysisType__synonyms", curie=CFDE_SCHEMA.curie('synonyms'),
                   model_uri=CFDE_SCHEMA.analysisType__synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.ncbiTaxonomy__id = Slot(uri=CFDE_SCHEMA.id, name="ncbiTaxonomy__id", curie=CFDE_SCHEMA.curie('id'),
                   model_uri=CFDE_SCHEMA.ncbiTaxonomy__id, domain=None, range=URIRef,
                   pattern=re.compile(r'^NCBI:txid[0-9]+$'))

slots.ncbiTaxonomy__clade = Slot(uri=CFDE_SCHEMA.clade, name="ncbiTaxonomy__clade", curie=CFDE_SCHEMA.curie('clade'),
                   model_uri=CFDE_SCHEMA.ncbiTaxonomy__clade, domain=None, range=str)

slots.ncbiTaxonomy__description = Slot(uri=CFDE_SCHEMA.description, name="ncbiTaxonomy__description", curie=CFDE_SCHEMA.curie('description'),
                   model_uri=CFDE_SCHEMA.ncbiTaxonomy__description, domain=None, range=Optional[str])

slots.ncbiTaxonomy__synonyms = Slot(uri=CFDE_SCHEMA.synonyms, name="ncbiTaxonomy__synonyms", curie=CFDE_SCHEMA.curie('synonyms'),
                   model_uri=CFDE_SCHEMA.ncbiTaxonomy__synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.anatomy__id = Slot(uri=CFDE_SCHEMA.id, name="anatomy__id", curie=CFDE_SCHEMA.curie('id'),
                   model_uri=CFDE_SCHEMA.anatomy__id, domain=None, range=URIRef)

slots.anatomy__description = Slot(uri=CFDE_SCHEMA.description, name="anatomy__description", curie=CFDE_SCHEMA.curie('description'),
                   model_uri=CFDE_SCHEMA.anatomy__description, domain=None, range=Optional[str])

slots.anatomy__synonyms = Slot(uri=CFDE_SCHEMA.synonyms, name="anatomy__synonyms", curie=CFDE_SCHEMA.curie('synonyms'),
                   model_uri=CFDE_SCHEMA.anatomy__synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.fileFormat__id = Slot(uri=CFDE_SCHEMA.id, name="fileFormat__id", curie=CFDE_SCHEMA.curie('id'),
                   model_uri=CFDE_SCHEMA.fileFormat__id, domain=None, range=URIRef)

slots.fileFormat__description = Slot(uri=CFDE_SCHEMA.description, name="fileFormat__description", curie=CFDE_SCHEMA.curie('description'),
                   model_uri=CFDE_SCHEMA.fileFormat__description, domain=None, range=Optional[str])

slots.fileFormat__synonyms = Slot(uri=CFDE_SCHEMA.synonyms, name="fileFormat__synonyms", curie=CFDE_SCHEMA.curie('synonyms'),
                   model_uri=CFDE_SCHEMA.fileFormat__synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.dataType__id = Slot(uri=CFDE_SCHEMA.id, name="dataType__id", curie=CFDE_SCHEMA.curie('id'),
                   model_uri=CFDE_SCHEMA.dataType__id, domain=None, range=URIRef)

slots.dataType__description = Slot(uri=CFDE_SCHEMA.description, name="dataType__description", curie=CFDE_SCHEMA.curie('description'),
                   model_uri=CFDE_SCHEMA.dataType__description, domain=None, range=Optional[str])

slots.dataType__synonyms = Slot(uri=CFDE_SCHEMA.synonyms, name="dataType__synonyms", curie=CFDE_SCHEMA.curie('synonyms'),
                   model_uri=CFDE_SCHEMA.dataType__synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.disease__id = Slot(uri=CFDE_SCHEMA.id, name="disease__id", curie=CFDE_SCHEMA.curie('id'),
                   model_uri=CFDE_SCHEMA.disease__id, domain=None, range=URIRef)

slots.disease__description = Slot(uri=CFDE_SCHEMA.description, name="disease__description", curie=CFDE_SCHEMA.curie('description'),
                   model_uri=CFDE_SCHEMA.disease__description, domain=None, range=Optional[str])

slots.disease__synonyms = Slot(uri=CFDE_SCHEMA.synonyms, name="disease__synonyms", curie=CFDE_SCHEMA.curie('synonyms'),
                   model_uri=CFDE_SCHEMA.disease__synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.phenotype__id = Slot(uri=CFDE_SCHEMA.id, name="phenotype__id", curie=CFDE_SCHEMA.curie('id'),
                   model_uri=CFDE_SCHEMA.phenotype__id, domain=None, range=URIRef)

slots.phenotype__description = Slot(uri=CFDE_SCHEMA.description, name="phenotype__description", curie=CFDE_SCHEMA.curie('description'),
                   model_uri=CFDE_SCHEMA.phenotype__description, domain=None, range=Optional[str])

slots.phenotype__synonyms = Slot(uri=CFDE_SCHEMA.synonyms, name="phenotype__synonyms", curie=CFDE_SCHEMA.curie('synonyms'),
                   model_uri=CFDE_SCHEMA.phenotype__synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.compound__id = Slot(uri=CFDE_SCHEMA.id, name="compound__id", curie=CFDE_SCHEMA.curie('id'),
                   model_uri=CFDE_SCHEMA.compound__id, domain=None, range=URIRef)

slots.compound__description = Slot(uri=CFDE_SCHEMA.description, name="compound__description", curie=CFDE_SCHEMA.curie('description'),
                   model_uri=CFDE_SCHEMA.compound__description, domain=None, range=Optional[str])

slots.compound__synonyms = Slot(uri=CFDE_SCHEMA.synonyms, name="compound__synonyms", curie=CFDE_SCHEMA.curie('synonyms'),
                   model_uri=CFDE_SCHEMA.compound__synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.substance__id = Slot(uri=CFDE_SCHEMA.id, name="substance__id", curie=CFDE_SCHEMA.curie('id'),
                   model_uri=CFDE_SCHEMA.substance__id, domain=None, range=URIRef)

slots.substance__description = Slot(uri=CFDE_SCHEMA.description, name="substance__description", curie=CFDE_SCHEMA.curie('description'),
                   model_uri=CFDE_SCHEMA.substance__description, domain=None, range=Optional[str])

slots.substance__synonyms = Slot(uri=CFDE_SCHEMA.synonyms, name="substance__synonyms", curie=CFDE_SCHEMA.curie('synonyms'),
                   model_uri=CFDE_SCHEMA.substance__synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.substance__compound = Slot(uri=CFDE_SCHEMA.compound, name="substance__compound", curie=CFDE_SCHEMA.curie('compound'),
                   model_uri=CFDE_SCHEMA.substance__compound, domain=None, range=Union[str, CompoundId])

slots.gene__id = Slot(uri=CFDE_SCHEMA.id, name="gene__id", curie=CFDE_SCHEMA.curie('id'),
                   model_uri=CFDE_SCHEMA.gene__id, domain=None, range=URIRef)

slots.gene__description = Slot(uri=CFDE_SCHEMA.description, name="gene__description", curie=CFDE_SCHEMA.curie('description'),
                   model_uri=CFDE_SCHEMA.gene__description, domain=None, range=Optional[str])

slots.gene__synonyms = Slot(uri=CFDE_SCHEMA.synonyms, name="gene__synonyms", curie=CFDE_SCHEMA.curie('synonyms'),
                   model_uri=CFDE_SCHEMA.gene__synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.gene__organism = Slot(uri=CFDE_SCHEMA.organism, name="gene__organism", curie=CFDE_SCHEMA.curie('organism'),
                   model_uri=CFDE_SCHEMA.gene__organism, domain=None, range=Union[str, NcbiTaxonomyId],
                   pattern=re.compile(r'^NCBI:txid[0-9]+$'))

slots.protein__id = Slot(uri=CFDE_SCHEMA.id, name="protein__id", curie=CFDE_SCHEMA.curie('id'),
                   model_uri=CFDE_SCHEMA.protein__id, domain=None, range=URIRef)

slots.protein__description = Slot(uri=CFDE_SCHEMA.description, name="protein__description", curie=CFDE_SCHEMA.curie('description'),
                   model_uri=CFDE_SCHEMA.protein__description, domain=None, range=Optional[str])

slots.protein__synonyms = Slot(uri=CFDE_SCHEMA.synonyms, name="protein__synonyms", curie=CFDE_SCHEMA.curie('synonyms'),
                   model_uri=CFDE_SCHEMA.protein__synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.protein__organism = Slot(uri=CFDE_SCHEMA.organism, name="protein__organism", curie=CFDE_SCHEMA.curie('organism'),
                   model_uri=CFDE_SCHEMA.protein__organism, domain=None, range=Optional[Union[str, NcbiTaxonomyId]],
                   pattern=re.compile(r'^NCBI:txid[0-9]+$'))

slots.proteinGene__protein = Slot(uri=CFDE_SCHEMA.protein, name="proteinGene__protein", curie=CFDE_SCHEMA.curie('protein'),
                   model_uri=CFDE_SCHEMA.proteinGene__protein, domain=None, range=Union[str, ProteinId])

slots.proteinGene__gene = Slot(uri=CFDE_SCHEMA.gene, name="proteinGene__gene", curie=CFDE_SCHEMA.curie('gene'),
                   model_uri=CFDE_SCHEMA.proteinGene__gene, domain=None, range=Union[str, GeneId])

slots.idNamespace__id = Slot(uri=CFDE_SCHEMA.id, name="idNamespace__id", curie=CFDE_SCHEMA.curie('id'),
                   model_uri=CFDE_SCHEMA.idNamespace__id, domain=None, range=URIRef)

slots.idNamespace__abbreviation = Slot(uri=CFDE_SCHEMA.abbreviation, name="idNamespace__abbreviation", curie=CFDE_SCHEMA.curie('abbreviation'),
                   model_uri=CFDE_SCHEMA.idNamespace__abbreviation, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-zA-Z0-9_]+$'))

slots.idNamespace__description = Slot(uri=CFDE_SCHEMA.description, name="idNamespace__description", curie=CFDE_SCHEMA.curie('description'),
                   model_uri=CFDE_SCHEMA.idNamespace__description, domain=None, range=Optional[str])