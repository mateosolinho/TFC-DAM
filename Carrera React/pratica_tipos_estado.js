import React from "react";

export default ({ name, lastname }) => {
  const [fullName, setFullName] = React.useState(`${name} ${lastname}`);

  return <p>{fullName}</p>;
};
