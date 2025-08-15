from enum import Enum

class OperatorEnum(Enum):
    AND = 'AND'
    OR = 'OR'

class PredicatesEnum(Enum):
    LIKE = 'LIKE'
    BEWTEEN = 'BEWTEEN'
    NOT = 'NOT'
    IN = 'IN'
    EXISTS = 'EXISTS'

class JoinTypeEnum(Enum):
    INNER = 'INNER'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    UNION = 'UNION'

class RelationShipTypeEnum(Enum):
    OneToOne: 'ONE_TO_ONE'
    ManyToOne: 'MANY_TO_ONE'
    ManyToMany: 'MANY_TO_MANY'


    